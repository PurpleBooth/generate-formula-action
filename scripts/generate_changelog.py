#!/usr/bin/env python3
"""Generate a changelog for a Homebrew formula PR.

Uses a three-tier fallback so a changelog is always produced:

1. **cog (cocogitto)** -- ``cog changelog --at <tag>``; produces the
   richest output from conventional commits.
2. **git log**         -- ``git log --oneline <prev>..<current>``; a
   plain commit list when cog fails or is unavailable.
3. **minimal message** -- a single-line header; the very last resort.

When run as a script, inputs come from environment variables::

    REPO_PATH     directory of the checked-out main repo
    CURRENT_TAG   the release tag, e.g. v6.1.0
    PREVIOUS_TAG  the previous release tag, e.g. v6.0.12
"""

from __future__ import annotations

import os
import subprocess

_CO_TIMEOUT = 120
_GIT_TIMEOUT = 60


def _try_cog(repo_path: str, current_tag: str, cog_bin: str) -> str | None:
    """Attempt to generate a changelog with cog. Return None on failure."""
    try:
        result = subprocess.run(
            [cog_bin, "changelog", "--at", current_tag],
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=_CO_TIMEOUT,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout
    return None


def _try_git_log(
    repo_path: str, current_tag: str, previous_tag: str | None
) -> str | None:
    """Attempt to generate a changelog with git log. Return None on failure."""
    if previous_tag:
        range_spec = f"{previous_tag}..{current_tag}"
    else:
        range_spec = current_tag
    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "--pretty=format:- %s",
                range_spec,
            ],
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=_GIT_TIMEOUT,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if result.returncode == 0 and result.stdout.strip():
        return f"## {current_tag}\n\n{result.stdout}\n"
    return None


def _minimal_fallback(current_tag: str) -> str:
    """Return a minimal changelog when all other methods fail."""
    return f"## {current_tag}\n\nUpdate to {current_tag}\n"


def generate_changelog(
    repo_path: str,
    current_tag: str,
    previous_tag: str | None = None,
    *,
    cog_bin: str = "cog",
) -> str:
    """Generate a changelog, trying cog, then git log, then a minimal message."""
    return (
        _try_cog(repo_path, current_tag, cog_bin)
        or _try_git_log(repo_path, current_tag, previous_tag)
        or _minimal_fallback(current_tag)
    )


def main() -> None:
    print(
        generate_changelog(
            repo_path=os.environ["REPO_PATH"],
            current_tag=os.environ["CURRENT_TAG"],
            previous_tag=os.environ.get("PREVIOUS_TAG"),
        ),
        end="",
    )


if __name__ == "__main__":
    main()
