# Evolution Protocol Specification (EP)

Status: Normative

This document defines the normative requirements for conformance with
Evolution Protocol (EP).

EP is a downstream specification that conforms to Structural Explainability (SE).
All SE neutrality constraints apply.

The primary object specified here is graph evolution.
EP defines a structural framework for representing
graphs, graph change, and graph histories
without embedding epistemic, causal, or normative interpretation.

## How to Read This Spec

Keywords MUST, MUST NOT, SHOULD, and MAY
are to be interpreted as described in RFC 2119.

Use of terms such as "canonical" denotes structural role only and
does not imply epistemic, causal, or normative preference.

This specification does not prescribe editorial structure,
terminology preference, or documentation layout beyond identifier semantics.

## Representation vs Constraint Classes

Some requirements describe what the substrate MAY represent,
while others constrain how such representations MUST NOT be interpreted.

Overlap between these classes is intentional:
representation permissions do not imply explanatory commitment.

## Identifier Semantics and Stability

Each requirement in this document is identified by a stable identifier
of the form `EP.*`.

Identifiers are the sole normative reference for conformance.
Textual wording MAY be clarified over time without changing meaning;
any change that alters the requirement MUST result in a new identifier.

Renaming, reordering, or relocating identifiers constitutes a semantic
change and is therefore intentionally diff-visible.

Repository paths, filenames, and section ordering are non-normative and
do not affect identifier meaning.

---

## EP.CONFORMANCE.SE.REQUIRED

Any system claiming conformance with this specification MUST also conform to
the Structural Explainability Specification.

EP MUST NOT weaken or override any SE neutrality constraints.

## EP.CONFORMANCE.AE.REQUIRED

Any system claiming conformance with this specification MUST also conform to
the Accountable Entities (AE) Specification.

EP MUST use AE entity kinds and identity regimes as the basis for graph nodes.

## EP.DEFINITION.CORE

Evolution Protocol defines a structural framework for representing graph
evolution over accountable entities.

EP specifies:

- graph form (nodes and edges)
- graph state (immutable snapshots)
- graph delta (structured change records)
- graph evolution (ordered histories of states and deltas)

EP does not specify interpretation, explanation, evaluation, or enforcement.

## EP.GRAPH.DEFINITION

A Graph consists of:

- nodes corresponding to Accountable Entities
- edges corresponding to structural relationships between nodes

Graphs MUST assert only structural existence and linkage.
Graphs MUST NOT assert epistemic truth, causal explanation, or normative judgment.

## EP.GRAPH.STATE

A Graph State is a snapshot of a Graph at a point in an ordered history.

Graph States MUST be immutable once recorded.
Graph States MUST be sufficient to support structural comparison.

Graph State identity and persistence MUST be explicit and structurally checkable.

## EP.GRAPH.DELTA

A Graph Delta records structural change between two Graph States.

A Graph Delta MUST be representable as a finite set of operations, including:

- node introduction or retirement
- edge addition or removal

Graph Deltas MUST NOT assert reasons for change.
Graph Deltas MUST NOT assert causal mechanisms.
Graph Deltas MUST NOT assert correctness, validity, or compliance.

## EP.GRAPH.EVOLUTION

Graph Evolution is an ordered sequence of Graph States connected by Graph Deltas.

Graph Evolution MUST:

- preserve AE identity regimes for all nodes across states
- preserve historical traceability without destructive overwrite
- support reconstruction of prior states from recorded history

Graph Evolution MUST NOT embed explanation.
Explanation MAY be attached only by external frameworks or downstream layers.

## EP.SCOPE.EXCLUSIONS

This does not define:

- domain vocabularies for relationship meaning
- causal models or explanatory mechanisms
- epistemic validation or truth evaluation
- normative judgment, compliance, or enforcement
- optimization, decision-making, or recommendation logic

These concerns are explicitly out of scope.
