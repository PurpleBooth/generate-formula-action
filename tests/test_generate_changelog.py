"""Tests for the changelog generator.

``generate_changelog`` produces a markdown changelog for a release using a
three-tier fallback:

1. **cog (cocogitto)** -- primary method, reads conventional commits
2. **git log**         -- fallback when cog fails or is unavailable
3. **minimal message** -- last resort when neither works

These tests verify each tier of the fallback independently.
"""

import subprocess
from pathlib import Path

import pytest

from generate_changelog import generate_changelog

FAKE_COG = "cog-binary-that-does-not-exist-12345"

# Isolate from the host's global git hooks, editor, and config so the
# fixture commits/tags never trigger pre-commit or tag hooks.
_GIT_ENV = {
    "GIT_AUTHOR_NAME": "Test",
    "GIT_AUTHOR_EMAIL": "test@example.com",
    "GIT_COMMITTER_NAME": "Test",
    "GIT_COMMITTER_EMAIL": "test@example.com",
    "GIT_EDITOR": "true",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_SYSTEM": "/dev/null",
}


def _git(args: list[str], cwd: Path) -> None:
    subprocess.run(
        ["git", *args], cwd=cwd, check=True, capture_output=True, env=_GIT_ENV
    )


def _make_git_repo(repo: Path) -> None:
    """Create a git repo with two tagged releases."""
    _git(["init", "-q"], repo)
    (repo / "a.txt").write_text("a")
    _git(["add", "."], repo)
    _git(["commit", "-q", "-m", "feat: first feature"], repo)
    _git(["tag", "v1.0.0"], repo)

    (repo / "b.txt").write_text("b")
    _git(["add", "."], repo)
    _git(["commit", "-q", "-m", "fix: important bug"], repo)
    _git(["tag", "v1.1.0"], repo)


# --- git-log fallback tier --------------------------------------------------


def test_git_log_fallback_when_cog_unavailable(tmp_path: Path) -> None:
    """When cog is missing, fall back to git log between the two tags."""
    repo = tmp_path / "repo"
    repo.mkdir()
    _make_git_repo(repo)

    result = generate_changelog(
        str(repo), "v1.1.0", "v1.0.0", cog_bin=FAKE_COG
    )

    assert "fix: important bug" in result
    assert "feat: first feature" not in result


def test_fallback_includes_version_header(tmp_path: Path) -> None:
    """The git-log fallback output has a markdown header with the tag."""
    repo = tmp_path / "repo"
    repo.mkdir()
    _make_git_repo(repo)

    result = generate_changelog(
        str(repo), "v1.1.0", "v1.0.0", cog_bin=FAKE_COG
    )

    assert result.startswith("## v1.1.0")


# --- minimal fallback tier --------------------------------------------------


def test_minimal_fallback_when_both_fail(tmp_path: Path) -> None:
    """When cog fails AND the directory isn't a git repo, get a minimal message."""
    repo = tmp_path / "not-a-repo"
    repo.mkdir()

    result = generate_changelog(
        str(repo), "v1.1.0", "v1.0.0", cog_bin=FAKE_COG
    )

    assert "v1.1.0" in result
    assert len(result) > 0


def test_minimal_fallback_has_header(tmp_path: Path) -> None:
    """The minimal fallback still has a markdown header."""
    repo = tmp_path / "not-a-repo"
    repo.mkdir()

    result = generate_changelog(
        str(repo), "v2.0.0", "v1.0.0", cog_bin=FAKE_COG
    )

    assert "## v2.0.0" in result


# --- cog primary tier -------------------------------------------------------


@pytest.mark.skipif(
    subprocess.run(["which", "cog"], capture_output=True).returncode != 0,
    reason="cog not installed",
)
def test_cog_success_returns_cog_output(tmp_path: Path) -> None:
    """When cog is available and succeeds, use its output verbatim."""
    repo = tmp_path / "repo"
    repo.mkdir()
    _make_git_repo(repo)

    result = generate_changelog(str(repo), "v1.1.0", "v1.0.0")

    assert "v1.1.0" in result
    assert "fix: important bug" in result
