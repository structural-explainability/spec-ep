# Evolution Protocol Identifiers (EP)

This document defines the stable requirement identifiers used by the
Evolution Protocol (EP) specification.

Identifiers are the sole normative reference mechanism.
Section ordering, formatting, and presentation are non-normative.

## Overview

Defines the structural representation of graph evolution
over Accountable Entities (AE),
without causal or interpretive commitment,
under the neutrality constraints of Structural Explainability (SE).

## Identifier Semantics and Ordering

Identifiers are the sole normative reference mechanism.
Section ordering, formatting, and presentation are non-normative.

Identifiers are listed in strict alphabetical order to remove
editorial discretion and ensure deterministic placement.

## Identifier Naming Rules

All identifiers follow this pattern:

EP.<CATEGORY>.<SUBCATEGORY>.<QUALIFIER>

Identifiers are:

- semantic, not positional
- stable across versions
- reusable across prose, code, and formal proofs
- language-agnostic
- suitable for direct mapping to Lean theorem names

Identifiers MUST NOT be renamed or repurposed.
New identifiers MAY be added only in a new major version of EP.

## Canonical Identifier List (Alphabetical, with Notes)

EP.CONFORMANCE.AE.REQUIRED

States that EP operates over Accountable Entities and their identity regimes.

EP.CONFORMANCE.SE.REQUIRED

States that EP conforms to the Structural Explainability specification.

EP.DEFINITION.CORE

Defines Evolution Protocol as a structural framework for representing
graph evolution over accountable entities.

EP.GRAPH.DEFINITION

Defines the structural form of graphs in EP.

EP.GRAPH.DELTA

Defines structured, non-causal graph change records.

EP.GRAPH.EVOLUTION

Defines ordered graph histories connecting states via deltas.

EP.GRAPH.STATE

Defines immutable graph snapshots in an ordered history.

EP.SCOPE.EXCLUSIONS

Defines what EP explicitly does not specify.

## Cross-Artifact Consistency Rule

Each identifier in this list MUST appear:

- exactly once in SPEC.md
- exactly once in CONFORMANCE.md
- exactly once as a field in the Lean ConformanceEvidence structure
- exactly once in the Lean requirements list

Alphabetical order SHOULD be preserved across all artifacts.
