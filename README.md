# Evolution Protocol (EP)

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
