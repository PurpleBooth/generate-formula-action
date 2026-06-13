"""Tests for the Homebrew formula template renderer.

The ``Generate the template`` step in ``action.yml`` renders a Jinja2
template (``formula.rb.j2``, supplied by the consuming repo) into a
concrete Homebrew formula by substituting three variables:

* ``github_repo`` -- the ``owner/name`` slug
* ``git_tag``      -- the release tag, e.g. ``v6.1.0``
* ``file_sha``     -- the sha256 of the release tarball

These tests pin that behaviour so the rendering can never silently drop
a variable or emit an unrendered ``{{ ... }}`` placeholder.
"""

from pathlib import Path

from render_template import render_formula

SAMPLE_TEMPLATE = """\
class TestFormula < Formula
  homepage "https://github.com/{{ github_repo }}"
  url "https://github.com/{{ github_repo }}/archive/{{ git_tag }}.tar.gz"
  sha256 "{{ file_sha }}"
end
"""


def _write_template(directory: Path) -> Path:
    template = directory / "formula.rb.j2"
    template.write_text(SAMPLE_TEMPLATE, encoding="utf-8")
    return template


def test_substitutes_github_repo(tmp_path: Path) -> None:
    template = _write_template(tmp_path)
    result = render_formula(
        str(template), "PurpleBooth/git-mit", "v6.1.0", "abc123"
    )
    assert "github.com/PurpleBooth/git-mit" in result


def test_substitutes_git_tag(tmp_path: Path) -> None:
    template = _write_template(tmp_path)
    result = render_formula(
        str(template), "PurpleBooth/git-mit", "v6.1.0", "abc123"
    )
    assert "archive/v6.1.0.tar.gz" in result


def test_substitutes_file_sha(tmp_path: Path) -> None:
    template = _write_template(tmp_path)
    result = render_formula(
        str(template), "PurpleBooth/git-mit", "v6.1.0", "deadbeef"
    )
    assert 'sha256 "deadbeef"' in result


def test_leaves_no_unrendered_placeholders(tmp_path: Path) -> None:
    template = _write_template(tmp_path)
    result = render_formula(
        str(template), "PurpleBooth/git-mit", "v6.1.0", "deadbeef"
    )
    assert "{{" not in result
    assert "}}" not in result


def test_handles_bare_filename_template(tmp_path: Path, monkeypatch) -> None:
    """A template path with no directory component resolves against cwd."""
    _write_template(tmp_path)
    monkeypatch.chdir(tmp_path)
    result = render_formula(
        "formula.rb.j2", "PurpleBooth/git-mit", "v6.1.0", "deadbeef"
    )
    assert 'sha256 "deadbeef"' in result
