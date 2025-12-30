# Conformance Checklist

This document defines the criteria for determining whether an artifact
conforms to the Evolution Protocol specification.

Identifiers referenced in this document are the sole normative reference.
Ordering and formatting are non-normative.

An artifact may be a specification, schema, implementation, repository,
or other deliverable claiming conformance.

## Conformance Overview

An artifact CONFORMS if and only if:

- all mandatory requirements are satisfied
- no prohibited assertions are present
- conformance with Structural Explainability (SE) and Accountable Entities (AE)
  is preserved

Failure of any single check constitutes non-conformance.

EP.CONFORMANCE.AE.REQUIRED

- [ ] Graph nodes correspond to Accountable Entities.
- [ ] AE identity regimes are preserved across graph evolution.
- Fail if: identity is redefined, merged, split, or overridden by graph change.

EP.CONFORMANCE.SE.REQUIRED

- [ ] The artifact explicitly claims conformance with Structural Explainability.
- [ ] No EP construct embeds epistemic, causal, or normative commitments.
- Fail if: SE neutrality constraints are weakened or bypassed.

EP.DEFINITION.CORE

- [ ] The artifact treats EP as a framework for graph evolution.
- [ ] Only graph, state, delta, and evolution constructs are defined.
- Fail if: EP is treated as an interpretive, transactional, or decision system.

EP.GRAPH.DEFINITION

- [ ] Graphs consist only of nodes and edges.
- [ ] Graphs assert only structural existence and linkage.
- Fail if: semantic meaning or interpretation is embedded in graph structure.

EP.GRAPH.DELTA

- [ ] Graph deltas record finite structural changes.
- [ ] Deltas do not assert reasons, causes, or correctness.
- Fail if: deltas explain, justify, or evaluate change.

EP.GRAPH.EVOLUTION

- [ ] Graph evolution is an ordered history of states and deltas.
- [ ] Prior states remain structurally accessible or reconstructible.
- Fail if: history is collapsed, rewritten, or destructively overwritten.

EP.GRAPH.STATE

- [ ] Graph states are immutable once recorded.
- [ ] Graph states support structural comparison.
- Fail if: states are mutable or overwritten in place.

EP.SCOPE.EXCLUSIONS

Verify that the artifact does not define:

- [ ] causal models
- [ ] epistemic validation or truth evaluation
- [ ] normative judgment or enforcement
- [ ] optimization, recommendation, or decision logic

Presence of any of the above constitutes non-conformance.

## Final Determination

An artifact CONFORMS if:

- all checks above pass, and
- no prohibited assertions are present.

Otherwise, the artifact is NON-CONFORMANT.

## Conformance Declaration

Artifacts claiming conformance SHOULD include a declaration of the form:

```text
Conforms to: AE Specification vX.Y
Conforms to: EP Specification vX.Y
Conforms to: SE Specification vX.Y
```
