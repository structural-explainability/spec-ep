# Conformance Checklist

This document defines the criteria for determining whether an artifact
conforms to the Evolution Protocol (EP) specification.

Identifiers referenced in this document are the sole normative reference.
Section ordering, formatting, and presentation are non-normative.

An artifact may be a specification, schema, implementation, repository,
or other deliverable claiming conformance.

## Conformance Overview

An artifact CONFORMS if and only if:

- all mandatory requirements are satisfied
- no prohibited assertions are present
- conformance with Structural Explainability (SE) is preserved
- conformance with Accountable Entities (AE) is preserved
- conformance with Governance Boundary (GB) is preserved where governance-related records are referenced
- conformance with Interpretation Boundary (IB) is preserved where interpretation may attach
- upstream transformation and persistence definitions are referenced without redefinition

Failure of any single check constitutes non-conformance.

## EP.CONFORMANCE.AE.REQUIRED

- [ ] Graph nodes reference Accountable Entities.
- [ ] AE kind mappings are preserved across graph evolution.
- [ ] Upstream SE profile-kind mappings are preserved across graph evolution.
- [ ] EP does not redefine accountable entity kinds, SE profile kinds, identity regimes,
- or persistence behavior.
- Fail if: AE kinds, SE profile kinds, identity regimes, or persistence behavior are
  redefined, merged, split, overridden, or made interpretation-dependent by graph evolution.

## EP.CONFORMANCE.GB.REQUIRED

- [ ] Governance-related records or actions preserve Governance Boundary constraints.
- [ ] Governance records, lifecycle labels, approvals, deprecations, supersessions, or
- provenance remain structural records only.
- [ ] Governance-related EP records do not assert authority, legitimacy, obligation,
- correctness, or enforcement.
- Fail if: governance-related records are treated as authority, legitimacy, obligation,
  correctness, endorsement, compliance, or enforcement.

## EP.CONFORMANCE.IB.REQUIRED

- [ ] Interpretation Boundary constraints are preserved.
- [ ] Interpretation is not embedded into graph structure, graph state, graph delta,
  transition, or history.
- [ ] Interpretive attachments are external and non-mutating.
- Fail if: interpretation modifies, replaces, or redefines graph structure, graph state,
  graph delta, transition, history, identity, persistence, or transformation references.

## EP.CONFORMANCE.SE.REQUIRED

- [ ] The artifact explicitly claims conformance with Structural Explainability.
- [ ] No EP construct weakens, overrides, or reinterprets SE neutrality constraints.
- [ ] EP constructs remain structural and do not embed epistemic, causal, normative,
  authoritative, legitimacy-bearing, obligation-bearing, or enforcement commitments.
- Fail if: SE neutrality constraints are weakened, bypassed, overridden, or reinterpreted.

## EP.DEFINITION.CORE

- [ ] The artifact treats EP as a structural protocol for accountable-entity graph records
- moving through time.
- [ ] EP scope is limited to graph form, graph state, graph delta, graph evolution history,
  structural comparison, and traceable references to upstream transformation
  and persistence classifications.
- [ ] EP does not define interpretation, explanation, evaluation, authority, legitimacy,
  obligation, enforcement, or decision logic.
- Fail if: EP is treated as an interpretive, explanatory, transactional, governance-authority,
  validation, enforcement, optimization, recommendation, or decision system.

## EP.GRAPH.DEFINITION

- [ ] Graphs consist of nodes referencing Accountable Entities and edges representing
  structural relationships between nodes.
- [ ] Graphs assert only structural existence and linkage.
- [ ] Graphs do not assert relationship meaning beyond structural linkage.
- Fail if: semantic meaning, interpretation, causal explanation, epistemic truth,
  normative judgment, authority, legitimacy, obligation, or enforcement is embedded in graph structure.

## EP.GRAPH.DELTA

- [ ] Graph deltas record finite structural changes between graph states.
- [ ] Graph deltas may record node introduction, node retirement, edge addition, edge removal,
  node attribute reference update, or edge attribute reference update.
- [ ] Graph deltas may reference upstream SE transformation families or operators.
- [ ] Graph deltas do not define transformation families, transformation operators, or
  transformation semantics.
- [ ] Graph deltas do not assert reasons, causes, correctness, validity, compliance,
  legitimacy, authority, or enforcement.
- Fail if: deltas explain, justify, evaluate, validate, authorize, enforce,
  or define transformation behavior.

## EP.GRAPH.EVOLUTION

- [ ] Graph evolution is an ordered sequence of graph states connected by graph deltas.
- [ ] Prior states remain structurally accessible or reconstructible.
- [ ] Historical traceability is preserved without destructive overwrite.
- [ ] AE kind/profile mappings are preserved unless an explicit structural delta records
  a permitted mapping-reference change.
- [ ] References to upstream transformation and persistence classifications remain traceable
  and are not redefined.
- Fail if: history is collapsed, rewritten, destructively overwritten, made non-traceable,
  or used to redefine AE, SE, transformation, or persistence behavior.

## EP.GRAPH.IDENTITY.NONDERIVATION

- [ ] Node continuity does not by itself imply SE identity persistence.
- [ ] Edge continuity does not by itself imply SE identity persistence.
- [ ] Graph-state continuity does not by itself imply SE identity persistence.
- [ ] Graph-history continuity does not by itself imply SE identity persistence.
- [ ] Persistence is referenced only through upstream SE persistence rules, profile-relative
  classification, or contract-defined persistence outcomes.
- Fail if: PRS, BRK, IGN, identity relevance, identity preservation, or identity breakage
  is inferred from graph continuity alone.

## EP.GRAPH.STATE

- [ ] Graph states are immutable once recorded.
- [ ] Graph states support structural comparison.
- [ ] Graph states are sufficient to support structural access to the recorded graph
  at that point in the ordered history.
- [ ] Graph state continuity is not treated as identity persistence unless persistence
  is separately established by upstream SE persistence rules.
- Fail if: graph states are mutable, overwritten in place, non-comparable, or used
  by themselves to assert identity persistence.

## EP.PERSISTENCE.REFERENCE

- [ ] EP may reference upstream SE persistence outcomes and classifications.
- [ ] Persistence references remain structurally explicit.
- [ ] Persistence references remain traceable to upstream SE contract artifacts.
- [ ] EP does not redefine PRS, BRK, IGN, identity relevance, identity irrelevance,
  identity preservation, identity breakage, or profile-relative persistence.
- Fail if: EP defines, modifies, infers, or reinterprets upstream persistence
  outcomes or persistence classification rules.

## EP.SCOPE.EXCLUSIONS

Verify that the artifact does not define:

- [ ] domain vocabularies for relationship meaning
- [ ] accountable entity kinds
- [ ] SE profile kinds
- [ ] identity regimes
- [ ] persistence outcomes
- [ ] transformation families or operators
- [ ] causal models or explanatory mechanisms
- [ ] epistemic validation or truth evaluation
- [ ] authority
- [ ] legitimacy
- [ ] obligation
- [ ] normative judgment, compliance, or enforcement
- [ ] optimization, decision-making, or recommendation logic
- [ ] governance lifecycle rules
- [ ] interpretation, explanation, evidence, or attestation interfaces

Presence of any excluded concern as an EP-defined construct constitutes non-conformance.

## EP.TRANSFORMATION.REFERENCE

- [ ] EP may reference upstream SE transformation families, operators, or classifications.
- [ ] Transformation references remain structurally explicit.
- [ ] Transformation references remain traceable to upstream SE contract artifacts.
- [ ] EP does not define transformation families, transformation operators,
  transformation semantics, or transformation classification rules.
- Fail if: EP defines, modifies, infers, or reinterprets upstream transformation families,
  operators, semantics, or classification rules.

## Final Determination

An artifact CONFORMS if:

- all checks above pass
- no prohibited assertions are present
- conformance with Structural Explainability is preserved
- conformance with Accountable Entities is preserved
- applicable Governance Boundary constraints are preserved
- applicable Interpretation Boundary constraints are preserved
- upstream transformation and persistence references remain traceable and non-redefining

Otherwise, the artifact is NON-CONFORMANT.

## Conformance Declaration

Artifacts claiming conformance SHOULD include a declaration of the form:

```text
Conforms to: EP Specification vX.Y
Conforms to: AE Specification vX.Y
Conforms to: GB Specification vX.Y
Conforms to: IB Specification vX.Y
Conforms to: SE Specification vX.Y
Conforms to: SE Transformation Contract vX.Y
Conforms to: SE Persistence Contract vX.Y
```
