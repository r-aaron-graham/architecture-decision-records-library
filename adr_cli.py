"""Simple CLI to create Architecture Decision Records (ADRs)."""

from __future__ import annotations

import datetime
import re
from pathlib import Path
from typing import Optional

import click


ADR_DIR = Path(__file__).resolve().parent / "adr"


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.strip().lower())
    return slug.strip("-")


def get_next_index() -> int:
    ADR_DIR.mkdir(exist_ok=True)
    indices = []
    for p in ADR_DIR.glob("*.md"):
        match = re.match(r"(\d+)-", p.name)
        if match:
            indices.append(int(match.group(1)))
    return max(indices) + 1 if indices else 1


@click.command()
@click.option("--title", required=True, help="Title of the decision.")
@click.option(
    "--status",
    default="proposed",
    show_default=True,
    type=click.Choice(["proposed", "accepted", "deprecated", "superseded"], case_sensitive=False),
    help="Status of the decision.",
)
def main(title: str, status: str) -> None:
    index = get_next_index()
    slug = slugify(title)
    filename = ADR_DIR / f"{index:04d}-{slug}.md"
    date = datetime.date.today().isoformat()
    content = f"# {index:04d}. {title}\n\n" + f"*Status: {status}\n*Date: {date}\n\n" + "## Context\n\n" + "## Decision\n\n" + "## Consequences\n\n" + "## Alternatives\n\n"
    with filename.open("w", encoding="utf-8") as f:
        f.write(content)
    click.echo(f"Created {filename}")


if __name__ == "__main__":  # pragma: no cover
    main()