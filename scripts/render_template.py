#!/usr/bin/env python3
"""Render a Homebrew formula from a Jinja2 template.

The consuming repository ships a ``formula.rb.j2`` template containing the
``github_repo``, ``git_tag`` and ``file_sha`` placeholders.  This module
renders it into a concrete ``.rb`` formula.

When run as a script it reads its inputs from environment variables, matching
the contract used by the ``Generate the template`` step in ``action.yml``::

    TEMPLATE_PATH  path to the .j2 template
    OUTPUT_FILE    where to write the rendered formula
    GITHUB_REPO    the owner/name slug
    GIT_TAG        the release tag, e.g. v6.1.0
    FILE_SHA       the sha256 of the release tarball
"""

from __future__ import annotations

import os
from jinja2 import Environment, FileSystemLoader


def render_formula(
    template_path: str, github_repo: str, git_tag: str, file_sha: str
) -> str:
    """Render the formula template at *template_path* and return the result."""
    env = Environment(
        loader=FileSystemLoader(os.path.dirname(template_path) or "."),
        keep_trailing_newline=True,
    )
    template = env.get_template(os.path.basename(template_path))
    return template.render(
        github_repo=github_repo,
        git_tag=git_tag,
        file_sha=file_sha,
    )


def main() -> None:
    output = render_formula(
        template_path=os.environ["TEMPLATE_PATH"],
        github_repo=os.environ["GITHUB_REPO"],
        git_tag=os.environ["GIT_TAG"],
        file_sha=os.environ["FILE_SHA"],
    )
    with open(os.environ["OUTPUT_FILE"], "w", encoding="utf-8") as handle:
        handle.write(output)


if __name__ == "__main__":
    main()
