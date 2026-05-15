# Evolution Protocol (EP)

[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/structural-explainability/spec-ep)
[![Tooling](https://img.shields.io/badge/python-3.15%2B-blue?logo=python)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

[![CI](https://github.com/structural-explainability/spec-ep/actions/workflows/ci-python.yml/badge.svg?branch=main)](https://github.com/structural-explainability/spec-ep/actions/workflows/ci-python.yml)
[![Links](https://github.com/structural-explainability/spec-ep/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/structural-explainability/spec-ep/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/structural-explainability/spec-ep/security)

> Authoritative specification of the Evolution Protocol (EP).

## Overview

The Evolution Protocol (EP) specification defines the structural requirements
for representing graph change over time.

EP specifies how structure may evolve while remaining neutral with respect to
epistemic truth, causal explanation, and normative judgment.

EP is defined as a downstream specification that conforms to
Structural Explainability (SE) and operates over Accountable Entities (AE).

## Purpose

The purpose of EP is to specify
**how structural relationships between entities may change over time**
in a way that preserves identity, traceability, and historical accessibility.

EP concerns graph structure, graph state, and graph change only.
It does not define interpretation, explanation, evaluation, or enforcement.

## Scope

This specification defines:

- the structural form of graphs over accountable entities
- immutable graph states representing snapshots in time
- structured graph deltas representing change
- ordered graph histories preserving prior structure

This specification does NOT define:

- domain semantics for relationships
- causal or explanatory models
- epistemic validation or truth claims
- normative judgment or enforcement
- optimization, decision-making, or recommendation logic

## Position in the Stack

EP operates within the Structural Explainability boundary.

- Structural Explainability (SE) defines admissible representational constraints.
- Accountable Entities (AE) define identity and persistence regimes.
- Evolution Protocol (EP) defines graph evolution over those identities.
- Contextual Evidence & Explanations (CEE) may be layered over EP histories.

EP introduces time and structural change, but not explanation.

## Relationship to Other Specifications

- EP **conforms to** the Structural Explainability specification.
- EP **depends on** Accountable Entities for node identity.
- EP provides the structural basis for downstream interpretive layers.
- No upstream specification depends on EP.

## Repository Contents

- [SPEC.md](./SPEC.md) - Normative specification
- [IDENTIFIERS.md](./IDENTIFIERS.md) - Stable requirement identifiers
- [CONFORMANCE.md](./CONFORMANCE.md) - Conformance checklist
- [ANNOTATIONS.md](./ANNOTATIONS.md) - Annotation standards
- [LICENSE](./LICENSE) - licensing terms
- [CITATION.cff](./CITATION.cff) - Citation metadata
- [CHANGELOG.md](./CHANGELOG.md) - Version history

## Clarifying Statement

Evolution Protocol represents **structural change**, not causal process.

Graph evolution records that structure changed and how it differs
across states, without asserting why the change occurred,
whether it was justified, or what it means.

EP makes change observable and reconstructible
while leaving explanation, evaluation, and judgment
to external frameworks.

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

Open a machine terminal where you want the project:

```shell
git clone https://github.com/structural-explainability/spec-ep

cd spec-ep
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.15
uv sync --extra dev --extra docs --upgrade

# install git hooks once per clone
uvx pre-commit install

# generate/check registry artifacts
uv run se-validate
uv run se-ref-export
uv run se-ref-export --check
uv run se-ref-validate
uv run se-validate --strict

# autofix and manual fix issues
git add -A
uvx pre-commit run --all-files
# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# do chores
uv run python -m pyright
uv run python -m pytest

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)

## Manifest

[SE_MANIFEST.toml](./SE_MANIFEST.toml)
