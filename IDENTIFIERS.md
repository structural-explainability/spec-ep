# Evolution Protocol Identifiers (EP)

This document defines the stable requirement identifiers used by the
Evolution Protocol (EP) specification.

Identifiers are the sole normative reference mechanism.
Section ordering, formatting, and presentation are non-normative.

## Overview

Defines the structural representation of accountable-entity graph states,
deltas, transitions, and histories over time,
without causal, epistemic, normative, governance-authority,
or interpretive commitment,
under the neutrality constraints of Structural Explainability (SE).

## Identifier Semantics and Ordering

Identifiers are the sole normative reference mechanism.
Section ordering, formatting, and presentation are non-normative.

Identifiers are listed in strict alphabetical order to remove
editorial discretion and ensure deterministic placement.

## Identifier Naming Rules

All identifiers follow this pattern:

All identifiers begin with `EP.` and use uppercase dot-separated semantic terms.

Identifiers are:

- semantic, not positional
- stable across versions
- reusable across prose, code, and formal proofs
- language-agnostic
- suitable for direct mapping to Lean theorem names

Identifiers MUST NOT be renamed or repurposed.
New identifiers MAY be added only in a new major version of this document.

## Identifier Notes

Each identifier MUST be followed by exactly one note.

- The note MUST be expressed as a single bullet.
- The bullet text MAY wrap across lines.
- No additional bullets, sublists, or structural markers are permitted.
- Notes are explanatory only and do not introduce additional requirements.

## Canonical Identifier List (Alphabetical, with Notes)

EP.CONFORMANCE.AE.REQUIRED

- States that EP operates over Accountable Entities and preserves AE kind/profile mappings.

EP.CONFORMANCE.GB.REQUIRED

- States that EP preserves Governance Boundary constraints for governance-related records and actions.

EP.CONFORMANCE.IB.REQUIRED

- States that EP preserves Interpretation Boundary constraints and prevents interpretive leakage
  into graph evolution records.

EP.CONFORMANCE.SE.REQUIRED

- States that EP conforms to the Structural Explainability specification.

EP.DEFINITION.CORE

- Defines Evolution Protocol as a structural protocol for representing accountable-entity
  graph records as they move through time.

EP.GRAPH.DEFINITION

- Defines the structural form of graphs in EP.

EP.GRAPH.DELTA

- Defines structured, non-causal graph change records.

EP.GRAPH.EVOLUTION

- Defines ordered graph histories connecting states through deltas.

EP.GRAPH.IDENTITY.NONDERIVATION

- States that graph continuity does not by itself imply SE identity persistence.

EP.GRAPH.STATE

- Defines immutable graph snapshots in an ordered history.

EP.PERSISTENCE.REFERENCE

- Defines how EP may reference upstream SE persistence outcomes without redefining them.

EP.SCOPE.EXCLUSIONS

- Defines what EP explicitly does not specify.

EP.TRANSFORMATION.REFERENCE

- Defines how EP may reference upstream SE transformation families or operators without redefining them.

## Cross-Artifact Consistency Rule

Each identifier in this list MUST appear:

- exactly once in SPEC.md
- exactly once in CONFORMANCE.md
- exactly once as a field in the Lean `ConformanceEvidence` structure
- exactly once in the Lean requirements list

Alphabetical order SHOULD be preserved across all artifacts.
