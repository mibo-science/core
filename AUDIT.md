# MIBO Pilot Core Repository Audit

**Audit date:** 2026-08-14

**Repository:** `mibo-research-pilot/core`

**Scope:** historical conceptual, methodological, and claim-development record of the MIBO Pilot

## Audit coverage

The audit reviewed every tracked file on `main` (`README.md`, `hierarchy.md`, `laws.md`, `LICENSE`, and `.gitignore`) and the complete eleven-commit history from 2026-05-05 through 2026-08-04. No Git history was rewritten. The sibling repositories were checked only to verify their public links and current merged `main` branches; they were not modified.

## Findings and treatment

| Classification | Finding | Treatment |
|---|---|---|
| 1. Current factual contradiction | `laws.md` described Day 14 as the first API-collected session and described a web-to-API transition. Pilot collection was API-based continuously from Day 1. | Corrected in active text, with a dated 2026-08-14 correction note. Counts, claim IDs, outputs, and claim lineage were not changed. The original wording remains visible in Git history. |
| 1. Current factual contradiction | The active English expansion used “Machine Information Behavior Observatory,” while the official current expansion is “MIBO — Machine Information Behavioral Observatory.” | Current explanatory prose now uses the official expansion. Pilot-era terminology remains identified and preserved as historical wording in `hierarchy.md`. |
| 1. Current factual contradiction | README licensing prose assigned CC0 to observation data and query sets even though this repository contains researcher-authored conceptual text and its only repository license is Apache-2.0. | README now describes the actual Apache-2.0 license for this repository and does not invent rights over provider outputs stored elsewhere. `LICENSE` is unchanged. |
| 2. Stale current explanation | README presented Day 13 / 244 as the latest verified Pilot boundary without clearly separating the Paper B freeze from the continuing Pilot. | README now identifies Day 13 / 244 as the Paper B evidence freeze and states that later pre-2026-09-01 observations remain Pilot observations outside the release. |
| 2. Stale current explanation | The `laws.md` header said its status ran only through Day 13 although the registry also contained Day 14 claim-history entries. | The header now identifies Day 13 / 244 specifically as the Paper B freeze and labels Day 14 entries as later Pilot material outside that freeze. |
| 2. Stale current explanation | README presented this historically named `core` repository as the home of the later MIBO Core program. | README now makes the historical Pilot scope and post-2026-09-01 firewall explicit. |
| 2. Stale current explanation | README linked to `canonical-definitions-v0.1.md`, which is absent from both the current tree and all reachable Git history. | Removed the broken reference. No file was reconstructed from memory. |
| 3. Legitimate historical terminology | `hierarchy.md` records early terminology including “Machine Information Behavior Observatory.” | Preserved under an explicit historical-status header, with current repository-level terminology listed separately. |
| 3. Legitimate historical terminology | The numbered “Law” vocabulary and status language belong to Pilot claim governance. | Preserved, with a prominent disclaimer explaining that these are provisional Pilot claims rather than universal or confirmatory laws. |
| 4. Historical claim requiring contextualization | Several “confirmed” or “strengthened” labels could be read beyond the observed services, queries, dates, and conditions. | Added a registry-wide evidentiary boundary; original Law IDs, claim formulations, status history, withdrawals, refutations, and anomalies remain visible. |
| 4. Historical claim requiring contextualization | Law VII and P16 preserve Pilot gender coding that was not a validated demographic measure. | Added a methodological note. No new gender coding or inference was added, and the historical counts were not strengthened. |
| 5. Duplication | README and `hierarchy.md` repeated field and method definitions. | Retained because README now supplies current orientation while `hierarchy.md` preserves conceptual history; their roles are explicitly distinguished. |
| 6. Obsolete future-planning material | The 2026-08-04 README imported later-program sentinel-panel, Frozen–Live, replication, G-theory, Satellite, and Network plans. | Removed from active repository documentation. The material remains in Git history and is not maintained or summarized here as a post-Pilot protocol. |
| 7. Preserve unchanged | Apache License 2.0 text in `LICENSE`. | Preserved byte-for-byte. No conflicting reuse terms or identifiable incompatible copied material were found in the conceptual documents. |
| 7. Preserve unchanged | `.gitignore` is a broad Python template. | Preserved unchanged. It is verbose but safely covers the new standard-library validator and contains no evidentiary content requiring removal. |
| 7. Preserve unchanged | Law IDs, candidate IDs, claim wording where historically meaningful, correction lineage, withdrawals, refutations, and nonconfirmation. | Preserved. Only scope notes and the false collection-transition wording were corrected. |
| 8. Deletion candidate | None. | No file is disposable and devoid of historical or operational value. No deletions are proposed. |

## Methodological interpretation

The Pilot developed Longitudinal Machine Observation, the OPEN Principles (Observation, Parallelism, Embedded openness, and Non-stationarity), and re-observability as conceptual and methodological objectives. It did not fully achieve later standards: early request parameters and raw outputs are incomplete, independent within-cell replication was absent, and multi-site replication was not implemented. These are preservation and design limitations, not grounds for relabeling the surviving observations as invalid.

## Cross-repository verification

- [`mibo-research-pilot/queries`](https://github.com/mibo-research-pilot/queries) resolves and provides the exact versioned Pilot stimuli.
- [`mibo-research-pilot/reports`](https://github.com/mibo-research-pilot/reports) resolves and provides the observation evidence, correction record, and Paper B evidence manifest.
- `mibo-research-pilot/core` provides historical conceptual, methodological, and claim-development context; it is not the primary raw dataset.

## License result

`LICENSE` contains the unmodified Apache License 2.0. Current README licensing language is consistent with it. This repository primarily contains researcher-authored conceptual text and does not assert provider rights over generated outputs.

## Unresolved limitations

- The core repository does not independently reproduce every observation-level count in the historical claim registry; those claims must be evaluated with the reports repository.
- Some Pilot claims retain historical “confirmed” or “strengthened” labels. The registry-wide disclaimer supplies their evidentiary boundary without falsifying their recorded status history.
- Historical gender coding lacks a validated demographic measurement protocol and is retained only as developmental record.
- No public DOI, arXiv identifier, or journal citation for Paper B was available for `CITATION.cff`; none was invented.
