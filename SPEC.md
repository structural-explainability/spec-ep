# Evolution Protocol Specification (EP)

Status: Normative

This document defines the normative requirements for conformance with
Evolution Protocol (EP).

EP is a downstream specification that conforms to Structural Explainability (SE).
All SE neutrality constraints apply.

EP defines a structural protocol for representing accountable-entity graph
records as they move through time.

The primary object specified here is graph evolution.
EP defines structural forms for graphs, graph states, graph deltas,
and graph histories without embedding epistemic, causal, normative,
governance-authority, or interpretive commitment.

## How to Read This Spec

Keywords MUST, MUST NOT, SHOULD, and MAY
are to be interpreted as described in RFC 2119.

Use of terms such as "canonical" denotes structural role only and
does not imply epistemic, causal, or normative preference.

This specification does not prescribe editorial structure,
terminology preference, or documentation layout beyond identifier semantics.

## Representation vs Constraint Classes

Some requirements describe what graph evolution structures MAY represent,
while others constrain how such representations MUST NOT be interpreted.

Overlap between these classes is intentional:
representation permissions do not imply explanatory, epistemic,
causal, normative, authoritative, or enforcement commitment.

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

## EP.CONFORMANCE.AE.REQUIRED

Any system claiming conformance with this specification MUST also conform to
the Accountable Entities (AE) specification.

EP graph nodes MUST reference accountable entities defined under AE.

EP MUST preserve AE kind mappings and upstream SE profile-kind mappings.

EP MUST NOT redefine accountable entity kinds, SE profile kinds,
identity regimes, or persistence behavior.

## EP.CONFORMANCE.GB.REQUIRED

Any system claiming conformance with this specification MUST preserve
Governance Boundary (GB) constraints for governance-related records and actions.

EP MUST NOT treat governance records, lifecycle labels, approvals,
deprecations, supersessions, or provenance as authority, legitimacy,
obligation, correctness, or enforcement.

## EP.CONFORMANCE.IB.REQUIRED

Any system claiming conformance with this specification MUST preserve
Interpretation Boundary (IB) constraints.

EP MUST NOT embed interpretation into graph structure, graph state,
graph delta, graph transition, or graph history.

Interpretation MAY attach only through non-mutating downstream or external
interpretive attachment mechanisms.

## EP.CONFORMANCE.SE.REQUIRED

Any system claiming conformance with this specification MUST also conform to
the Structural Explainability (SE) specification.

EP MUST NOT weaken, override, or reinterpret any SE neutrality constraints.

## EP.DEFINITION.CORE

Evolution Protocol defines a structural protocol for representing
accountable-entity graph records as they move through time.

EP specifies:

- graph form
- graph state
- graph delta
- graph evolution history
- structural comparison across graph states
- references to upstream transformation and persistence classifications

EP does not specify interpretation, explanation, evaluation, authority,
legitimacy, obligation, enforcement, or decision logic.

## EP.GRAPH.DEFINITION

A graph consists of:

- nodes referencing Accountable Entities
- edges representing structural relationships between nodes

Graphs MUST assert only structural existence and linkage.

Graphs MUST NOT assert epistemic truth, causal explanation,
normative judgment, governance authority, legitimacy, obligation,
or enforcement.

## EP.GRAPH.DELTA

A graph delta records structural change between two graph states.

A graph delta MUST be representable as a finite structural change record,
including but not limited to:

- node introduction
- node retirement
- edge addition
- edge removal
- node attribute reference update
- edge attribute reference update

Graph deltas MAY reference upstream SE transformation families or operators.

Graph deltas MUST NOT define transformation families or operators.

Graph deltas MUST NOT assert reasons for change, causal mechanisms,
correctness, validity, compliance, legitimacy, authority, or enforcement.

## EP.GRAPH.EVOLUTION

Graph evolution is an ordered sequence of graph states connected by graph deltas.

Graph evolution MUST:

- preserve historical traceability without destructive overwrite
- support reconstruction or structural access to prior states
- preserve AE kind/profile mappings unless an explicit structural delta records
  a permitted mapping-reference change
- preserve references to upstream transformation and persistence classifications
  without redefining them

Graph evolution MUST NOT embed explanation or interpretation.

Explanation and interpretation MAY attach only through downstream or external
mechanisms that preserve IB non-mutation requirements.

## EP.GRAPH.IDENTITY.NONDERIVATION

Node continuity, edge continuity, graph-state continuity, or graph-history
continuity MUST NOT by itself imply SE identity persistence.

Identity persistence MAY be referenced only through upstream SE persistence
rules, profile-relative classification, or contract-defined persistence
outcomes.

EP MUST NOT infer PRS, BRK, IGN, identity relevance, identity preservation,
or identity breakage from graph continuity alone.

## EP.GRAPH.STATE

A graph state is an immutable snapshot of a graph at a point in an ordered
history.

Graph states MUST be immutable once recorded.

Graph states MUST be sufficient to support structural comparison.

Graph state continuity MUST NOT be treated as identity persistence unless
persistence is separately established by upstream SE persistence rules.

## EP.PERSISTENCE.REFERENCE

EP MAY reference upstream SE persistence outcomes and classifications.

EP MUST NOT redefine:

- PRS
- BRK
- IGN
- identity relevance
- identity irrelevance
- identity preservation
- identity breakage
- profile-relative persistence

Persistence references MUST remain structurally explicit and traceable to
upstream SE contract artifacts.

## EP.SCOPE.EXCLUSIONS

This specification does not define:

- domain vocabularies for relationship meaning
- accountable entity kinds
- SE profile kinds
- identity regimes
- persistence outcomes
- transformation families or operators
- causal models or explanatory mechanisms
- epistemic validation or truth evaluation
- authority
- legitimacy
- obligation
- normative judgment, compliance, or enforcement
- optimization, decision-making, or recommendation logic
- governance lifecycle rules
- interpretation, explanation, evidence, or attestation interfaces

These concerns are explicitly out of scope.

## EP.TRANSFORMATION.REFERENCE

EP MAY reference upstream SE transformation families, operators, or
classifications.

EP MUST NOT define transformation families, transformation operators,
transformation semantics, or transformation classification rules.

Transformation references MUST remain structurally explicit and traceable to
upstream SE contract artifacts.
