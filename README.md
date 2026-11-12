# Architecture Decision Records Library

This repository provides templates and examples for documenting
architecture decisions using the Architecture Decision Record (ADR)
format.  ADRs capture important technical choices, their context,
alternatives considered, and the consequences of the decision.  This
library can serve as a starting point for your own ADRs and as a
reference for how to structure them.

## What is an ADR?

An Architecture Decision Record documents a single key decision with
the following sections:

- **Context** – background information and forces influencing the
  decision.
- **Decision** – the choice that was made.
- **Status** – e.g., proposed, accepted, deprecated.
- **Consequences** – implications of the decision (trade‑offs).
- **Alternatives** – other options considered and reasons for not
  choosing them.

See [adr/0001-sample-decision.md](adr/0001-sample-decision.md) for an
example.

## Using the CLI

Install the dependency with `python -m pip install -r requirements.txt`.
This repository includes a simple CLI (`adr_cli.py`) to create new
ADR files.  To create a new record:

```bash
python adr_cli.py --title "Use PostgreSQL for metadata store" --status "accepted"
```

The script will generate a new file in the `adr/` directory with an
incremented number and the provided title. Open the generated file to fill
in the context, decision, trade-offs, and alternatives. The bundled example
shows how those sections fit together.

## Conventions

ADR files are numbered sequentially and stored under the `adr/`
directory.  Filenames are prefixed with a zero‑padded index followed
by a slugified version of the title.  ADRs should be stored in
version control alongside the codebase they document.