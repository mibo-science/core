# Historical MIBO Pilot Claim Registry

**Repository:** `mibo-research-pilot/core`

**Paper B evidence freeze:** Day 1–Day 13 — 2026-05-05 through 2026-07-28

**Paper B included observations:** 244

**Collection surface:** API from Day 1 — 2026-05-05

**Query set:** Pilot operational v0.1.1

Later Day 14 entries are preserved as continuing pre-2026-09-01 Pilot claim history and are outside the Paper B evidence freeze.

> **Historical status:** The term “Law” is historical MIBO Pilot terminology. A Pilot Law is a provisional, corrigible longitudinal claim generated during developmental observation. It is not a universal law of nature, a validated scale, a causal law, or a confirmatory post-Pilot result.

This registry preserves the original Law IDs, claim lineage, corrections, anomalies, withdrawals, refutations, weakening, and nonconfirmation. Its claims are bounded to the observed services, queries, conditions, and dates. Status labels record Pilot-era claim-governance decisions and do not establish factual correctness, population representativeness, permanent model traits, or generalization beyond that evidence.

## Epistemic rule

A numbered MIBO law is provisional.

It must survive repeated synchronized observation, prospective testing where applicable, provenance review, and later contradiction checks.

A law may be:

- refined;
- strengthened;
- weakened;
- bounded;
- superseded;
- withdrawn.

The registry uses Pilot-supported status terms such as candidate, supported, strengthened, weakened, revised, withdrawn, refuted, insufficient evidence, and historical only where the surviving record supports them. Existing historical labels are retained rather than silently recoded.

A candidate proposition is not a law.

A transcription, data-entry, or correction event is not model behavior.

---

## Pilot laws retained in the registry

“Confirmed” and similar labels below are historical Pilot statuses, not claims of universal, causal, or post-Pilot confirmation.

### Law I — Canonical Inclusion

Fixed queries can produce durable canonical inclusion cores.

Canonical inclusion does not require:

- immutable order;
- identical peripheral selections;
- identical explanation style;
- permanent universal inclusion across every wave.

The Day 11–Day 13 q001 record shows that a stable four-product nucleus can temporarily expand to five and contract again.

**Pilot-era formulation**:

> Fixed information situations can produce durable canonical inclusion cores while peripheral entities and ordinal positions fluctuate.

**Status:** Confirmed; interpretation refined.

---

### Law II — Perplexity URL Stability

Perplexity source behavior is multi-lag and source-regime-sensitive.

Required measurements include:

- normalized-URL survival from the immediately preceding wave;
- longer-lag recurrence;
- terminal-list length;
- retained URLs as a share of the current list;
- inline-used source set;
- source-list utilization;
- citation-index reassignment.

Day 13 evidence available in the verified comparison ledger:

- q001 retained 18/20 Day 12 URLs and returned to the full Day 11 terminal set;
- q004 retained 19/20 Day 12 URLs and returned to the full Day 11 terminal set;
- q005 retained 19/20 Day 12 URLs;
- citation numbers changed despite normalized-URL continuity.

The complete Day 12 raw URL baselines for q002 and q003 are not present in the current full-text packet, so Day 12→Day 13 aggregate retention is not reported.

**Pilot-era formulation**:

> Perplexity URL continuity must be measured across multiple lags and separately from terminal-list length, inline use, citation index, and answer-state recurrence.

**Status:** Continuing.

---

### Law III — Day 2 Anomaly

Multiple content features deviated together on 2026-05-12 and reverted in the next synchronized wave.

The evidence supports a localized common anomaly rather than a recurring abstraction cycle.

**Status:** Confirmed.

---

### Law VI — Per-Model Signature

Within the observed Pilot services and responses, systems showed recognizable response signatures, including:

- structural organization;
- caveats;
- recommendation framing;
- follow-up questions;
- evaluation vocabularies;
- implementation style;
- safety language.

These signatures coexist with changing entities, numerical parameters, source sets, and ordinal positions.

**Status:** Confirmed.

---

### Law VII — Gender Dominance in Person Queries

> **Methodological note:** Historical Pilot gender coding is preserved as part of the developmental record and should not be treated as a validated demographic measure. The registry does not add new gender inference or infer gender from names or appearance.

Japanese AI researcher queries remain overwhelmingly male-presenting in their five-person main lists.

Female-presenting inclusion has been:

- rare;
- intermittent;
- distributed across more than one system;
- variable in the person selected;
- unstable across consecutive observations.

Cumulative after Day 13:

- male-presenting main-list mentions: **215/220**;
- female-presenting main-list mentions: **5/220**.

Days 12 and 13 together produced:

- male-presenting: **40/40**;
- female-presenting: **0/40**.

Day 14 (a continuing API-collected Pilot session) produced:

- male-presenting: **19/20**;
- female-presenting: **1/20** — Arai Noriko (新井紀子), this session inside Claude's five-person main list rather than a supplementary section.

Cumulative after Day 14:

- male-presenting main-list mentions: **234/240**;
- female-presenting main-list mentions: **6/240**.

Supplementary names outside the requested five-person main list are not included in the official Law VII count.

**Status:** Strengthened.

---

### Law VIII — Absence of Stable Direct Academic Grounding

Within the fixed Pilot instrument, Perplexity frequently supplies web citations but has not established stable direct grounding in peer-reviewed papers, arXiv papers, or first-party scholarly profiles.

Observed source classes include:

- public-health and government sources;
- institutional sources;
- technical documentation;
- vendor-authored content;
- comparison media;
- user-generated platforms;
- video sources;
- aggregators.

The presence of a public or institutional source in a terminal list does not by itself establish that it supports the answer body.

Day 14 (a continuing API-collected Pilot session): Perplexity's terminal sources — read from the API `citations` array in the preserved packet — spanned comparison media, video (YouTube), health and institutional sources, and aggregators (Wikipedia), with zero peer-reviewed, arXiv, or first-party scholarly citations in that observation, consistent with the Pilot-era claim.

**Status:** Confirmed under continuing source-class audit.

---

### Law IX — Perplexity Inline Citation Shift

Beginning on Day 4, Perplexity attached inline numeric citations to answer claims while also supplying terminal source lists.

Cumulative after Day 13:

- **50/50** Perplexity observations since Day 4 contained inline numeric citations and terminal source lists.

Day 14 (a continuing API-collected Pilot session): inline numeric citations were present on **5/5** responses. In the preserved Day 14 packet, the terminal source list is delivered by the Perplexity API in a structured `citations` array (q001–q005: 20, 20, 19, 20, 20 sources) rather than rendered in the answer text; counting these, inline-plus-terminal continuity reaches **55/55** since Day 4.

Twenty-source regime:

- Day 11: 5/5;
- Day 12: 5/5;
- Day 13: 5/5;
- Day 14: 4/5 (q003 returned 19);
- total: **19/20**.

Instrument note: Pilot collection was API-based continuously from Day 1. In the preserved Day 14 Perplexity packet, inline citation markers remain in the answer body while the terminal source list is represented in the API `citations` array; coding for that packet reads terminal sources from the array.

Across Days 11–13:

- sources listed: 300;
- sources used inline: 115;
- aggregate utilization: 38.3%.

The interface-level citation form remains stable even when:

- terminal-list length changes;
- source utilization changes;
- normalized URLs change or recur;
- recommendation sets change;
- code depth changes;
- answer structures change.

**Status:** Confirmed / continuing.

---

## Withdrawn laws

### Law IV — Vendor-Official URL Ascendancy

The apparent monotonic increase in vendor-official URLs was a short-series artifact.

**Status:** Withdrawn.

### Law V — Perplexity Compression

Response length and compression showed no stable directional trend across queries.

**Status:** Withdrawn.

### Law X — GPT Product-Slot Biweekly Pattern

The proposed alternating product-slot pattern failed reverse-direction prediction.

Later A–B–A or present–absent sequences are treated as recurrence or candidate alternation, not periodic law, unless they survive repeated prospective tests.

**Status:** Withdrawn.

---

## Refuted hypothesis

### P12 — Parallel Abstraction Shift

A temporary reduction in numerical specificity appeared on Day 2 and did not reproduce consistently in later observations.

**Status:** Refuted.

---

## Historical candidates P13–P17

These candidates were introduced on Day 8 and remain part of the claim lineage.

### P13 — Inclusion Stability with Ordinal Instability

A recommendation or person set can remain stable while order changes across systems or waves.

Day 13 support includes:

- GPT q005 retaining stable inclusion anchors while ordinal positions changed;
- q001 retaining a shared top set with system-specific order.

**Status:** Active / supported.

### P14 — Brand-Family Convergence Before Exact-Product Convergence

Systems may converge at vendor-family level before converging on an exact product variant.

Day 13 q002 expands this idea into the more general P32.

**Status:** Incorporated into P32.

### P15 — Stable Citation Regime, Variable Citation Coverage

Perplexity’s citation format can remain stable while source-list utilization, URL sets, and answer content vary.

This proposition is now represented by Law IX and P29.

**Status:** Incorporated into Law IX and P29.

### P16 — Rare and Unstable Female Inclusion

Female-presenting researchers may appear in one observation and disappear later without changing the strongly male-dominant structure.

This proposition is now incorporated into Law VII.

**Status:** Incorporated into Law VII.

### P17 — Implementation Depth and Attribution Are Orthogonal

Code depth does not determine whether external attribution is provided.

Day 13 again shows:

- deeper runnable code without external attribution in non-search systems;
- external citations with non-runnable pseudocode in Perplexity.

**Status:** Active / supported.

---

## Active and bounded candidates P18–P34

### P18 — Session-Wide Response-State Recurrence

Multiple systems and queries can return in one wave to states observed at an earlier lag.

**Status:** Active / supported.

### P19 — Lag-Sensitive Stability

Behavior may appear unstable at lag 1 while recurring at a longer lag.

**Status:** Active / supported.

### P20 — Response-Packet Coupling

A returning answer template may carry entities, parameters, safety language, citation use, and defects together.

**Status:** Active / supported.

### P21 — Shared-Core Contraction

A universal cross-system set can shrink while preserving its most durable members.

This one-direction formulation is subsumed by the broader P27.

**Status:** Superseded by P27.

### P22 — Exact-Product Canonical Convergence

A family-level canonical can later converge at exact-product level.

Day 11–Day 12 CRM results supported this transition, but Day 13 shows that it can reverse.

**Status:** Incorporated into P28 and P32.

### P23 — Twenty-Source Terminal-List Regime

Perplexity can adopt a fixed expanded terminal-list length across all fixed queries while using only a subset inline.

Day 11–Day 13 support: **15/15** queries with 20 terminal sources.

**Status:** Strengthened.

### P24 — Cross-System Implementation–Explanation Gap

Multiple systems can recommend the same production feature without fully connecting it to their own implementation examples.

Day 13 q004:

| Feature | Recommended | Fully implemented |
|---|---:|---:|
| Metadata filtering | 4/4 | 0/4 |
| Hybrid retrieval | 4/4 | 0/4 |
| Reranking | 4/4 | 0/4 |

**Status:** Strengthened.

### P25 — Non-Search Advice-Slot Suppression

Multiple non-search systems can omit the same previously common advice slot within one wave.

The Day 11 nap omission did not persist. Nap guidance returned across all four systems by Day 13.

**Status:** Bounded / weakened.

### P26 — Response-State Recombination

A later response can combine elements from multiple prior states rather than reproduce one earlier packet exactly.

**Status:** Active / supported.

### P27 — Shared-Core Elasticity

A stable cross-system nucleus can expand when a peripheral item becomes universal and contract again when it exits one system.

Day 11–Day 13 q001 universal-set size:

```text
4 → 5 → 4
```

This proposition replaces the narrower Day 12 label “Shared-Core Re-expansion.”

**Status:** Revised / strengthened.

### P28 — Exact-Product Canonical Persistence

Exact-product convergence can persist across consecutive waves.

HubSpot CRM, Zoho CRM, and Pipedrive were universal on Days 11–12. Zoho CRM fell to 3/4 on Day 13 because Perplexity selected Bigin by Zoho CRM.

**Status:** Supported but bounded to two consecutive waves.

### P29 — Source-Regime Persistence

After a source-list regime transition, list length and much of the normalized source inventory can persist.

The twenty-source regime reached 15/15 observations across three waves.

**Status:** Strengthened.

### P30 — Alternation Termination by State Persistence

An apparent alternating sequence can stop when one state persists for two consecutive waves.

Day 13 support includes:

- GPT q001 retaining Asana before Trello;
- Gemini q002 retaining Monday before Salesforce;
- Claude q005 keeping 新井紀子 absent rather than continuing the prior present–absent sequence.

**Status:** Strengthened.

### P31 — Stable Source Set with Recommendation Substitution

A highly stable source inventory can coexist with changing recommendations or named entities.

Day 13 q005 retained the same six inline-used URLs while changing one main-list researcher.

**Status:** Strengthened.

### P32 — Granularity-Dependent Convergence

Cross-system convergence can contract at exact-product level while expanding at vendor-family level.

Day 13 q002:

- universal exact products: HubSpot CRM and Pipedrive;
- universal families: HubSpot, Zoho, Pipedrive, Salesforce.

**Status:** New / supported.

### P33 — Advice-Slot Convergence without Parameter Convergence

Systems can converge on whether an advice category is present while retaining different numerical or operational parameters.

Day 13 q003:

- nap guidance: 4/4;
- duration and timing: heterogeneous.

**Status:** New / supported.

### P34 — Source-State Recurrence without Response-State Recurrence

A prior terminal URL set can recur without restoring the prior recommendation set, rank order, source-use density, or prose structure.

Day 13 support:

- Perplexity q001 returned to its Day 11 terminal source set;
- Perplexity q004 returned to its Day 11 terminal source set;
- neither query restored the full Day 11 answer state.

**Status:** New / supported.

---

## Correction history relevant to the claim registry

### Day 12 Claude q003

The initially submitted Claude q003 record duplicated the GPT response because of an input error.

The correct Claude response was later supplied and replaced the duplicate.

Treatment:

- official Day 12 observation count remains 20;
- cumulative after Day 12 remains 224;
- the duplicate is not treated as cross-model behavior;
- the former duplicate-response candidate was deleted.

### Candidate numbering

After deletion of the erroneous collision candidate:

- Alternation Termination by State Persistence became P30;
- Stable Source Set with Recommendation Substitution became P31;
- Day 13 additions begin at P32.

### GPT q004 example date

The example metadata date was aligned to each declared observation date.

No capture-time or retrospective-generation inference is made from the example date.

### Collection and repository identifiers

- collection has been API-based since Day 1;
- the official GitHub organization is `mibo-research-pilot`.

The former Day 14-as-first-API description was factually incorrect and was corrected on 2026-08-14. This provenance correction changes no observation count, output, or other claim-history entry.

---

## Promotion criteria for candidates

A candidate should not be promoted solely because it appears several times retrospectively.

Promotion requires, where applicable:

1. a frozen operational definition;
2. prospective predictions;
3. repeated survival across later synchronized waves;
4. robustness to model, service-lineage, and retrieval changes;
5. provenance validation;
6. source and coding reproducibility;
7. explicit contradiction tests;
8. a documented claim-boundary decision.

---

## Historical scope boundary

This registry belongs to the developmental MIBO Pilot.

Paper B freezes evidence at Day 13 / 244 included observations. Later pre-2026-09-01 observations remain part of the developmental Pilot but are outside that evidence release. Nothing in this registry is a confirmatory result or normative protocol for the separate post-2026-09-01 MIBO Core program.
