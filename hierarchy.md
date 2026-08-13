# Historical MIBO Pilot Field and Terminology Development

> **Status notice:** This document preserves conceptual and terminology development from the MIBO Pilot. It is a historical record, not the normative field hierarchy or organizational design of the separate post-2026-09-01 MIBO Core program. Pilot-era wording is retained where changing it would obscure provenance.

Current repository-level explanatory prose uses:

- **MIBO — Machine Information Behavioral Observatory**;
- **Machine Behavioral Sciences**;
- **Machine Information Behavioral Sciences**;
- **machine information behavior**;
- **Longitudinal Machine Observation (LMO)**.

Earlier wording below, including “Machine Information Behavior Observatory,” documents the Pilot's terminology development rather than a current normative naming rule.

## Preserved Pilot-era field hierarchy

The Pilot positioned MIBO as an observation facility within **Machine Information Behavioral Sciences**, a specialized field under the broader umbrella of **Machine Behavioral Sciences**.

```text
Machine Behavioral Sciences
└── Machine Information Behavioral Sciences
    ├── Longitudinal Machine Observation (LMO)
    ├── source-attribution and citation-like behavior
    └── Machine Information Behavior Observatory (MIBO)
```

## 1. Parent field: Machine Behavioral Sciences

**Machine Behavioral Sciences** is the proposed umbrella field for the systematic study of machines as observable behavioral entities.

The field does not assume that machines possess consciousness, intention, or human-like mental states. Instead, it studies observable regularities in machine behavior: how machine systems respond, adapt, coordinate, recommend, rank, omit, explain, attribute, and interact under different inputs and environments.

In this usage, **behavior** means an observable input-output pattern produced by a machine system in a given technical, social, and informational environment.

Machine Behavioral Sciences draws on three broad traditions:

1. **Machine Behavior research** — the study of AI systems as behavioral objects.
2. **Behavioral Sciences** — empirical traditions for studying observable behavior, interaction, adaptation, and decision patterns.
3. **Domain-specific behavioral sciences of machines** — specialized areas such as machine information behavior, machine economic behavior, machine social behavior, and machine communication behavior.

## 2. Specialized field: Machine Information Behavioral Sciences

**Machine Information Behavioral Sciences** is the specialized field that studies how machine systems handle information.

It asks questions such as:

- What information do machines retrieve?
- What information do they select, rank, recommend, or omit?
- Which sources do they attribute, cite, or make visible?
- Which entities, domains, countries, organizations, and voices are amplified or forgotten?
- How do these patterns change across languages, models, interfaces, and time?

A concise definition:

> Machine Information Behavioral Sciences studies how machine systems retrieve, select, attribute, recommend, rank, omit, synthesize, transmit, and forget information over time.

This field is positioned at the intersection of:

```text
Machine Behavior research
× Information Behavior research
× Behavioral Sciences
```

## 3. Relationship to Information Behavior research

Traditional **Information Behavior** research has primarily studied human information needs, seeking, browsing, foraging, use, and sense-making.

Machine Information Behavioral Sciences extends this tradition to machine systems that now act as information intermediaries. Generative AI systems, search systems, recommendation systems, and agentic systems increasingly mediate what users see, cite, trust, and act upon.

The purpose is not to treat machines as humans. The purpose is to make machine information behavior observable, comparable, and historically traceable.

## 4. Relationship to GEO, SEO, AEO, and LLMO

SEO, GEO, AEO, and related optimization practices usually ask:

> How can a human, organization, or content producer become more visible to search engines or generative engines?

Machine Information Behavioral Sciences asks a different question:

> How do machine systems allocate informational visibility in the first place?

This creates a shift:

| Optimization paradigm | Observation paradigm |
|---|---|
| Intervene in engines | Observe engine behavior |
| Improve one actor's visibility | Study visibility allocation itself |
| Cross-sectional measurement | Longitudinal observation |
| Engineering and marketing focus | Scientific and descriptive focus |

MIBO therefore complements GEO rather than replacing it. GEO asks how to be cited by generative engines; MIBO asks how generative engines cite, recommend, and forget.

## 5. Core methodology: Longitudinal Machine Observation (LMO)

**Longitudinal Machine Observation (LMO)** is the core methodology used by MIBO.

LMO is defined as:

> Standardized longitudinal elicitation and observation of machine systems using repeated queries, repeated model observations, timestamped outputs, and versioned metadata.

The term **elicitation** is important. MIBO does not observe machine behavior passively in the same way an astronomer observes a star. It uses standardized prompts or queries to elicit machine responses, then records and compares those responses over time.

A basic LMO unit contains:

- a versioned query;
- a model or system identifier;
- an observation date and, when available, a precise timestamp;
- the interface or API used;
- the raw output;
- source-attribution or citation-like signals;
- extracted entities, products, organizations, or domains;
- notes on limitations and uncertainty.

### Methodological-development note

During the Pilot, LMO, the OPEN Principles, and re-observability were developing concepts rather than a fully validated measurement design. The OPEN Principles were articulated as **Observation**, **Parallelism**, **Embedded openness**, and **Non-stationarity**. Re-observability was developed as an epistemic and methodological objective; incomplete early request-parameter and raw-output preservation, the absence of independent within-cell replication, and the absence of multi-site replication limited its implementation during the Pilot and informed later formalization.

## 6. First research focus: source-attribution and citation-like behavior

MIBO's first research focus is **source-attribution and citation-like behavior** in generative AI systems.

This phrase is deliberately cautious. Generative AI source display is not identical to scholarly citation. A URL, source card, web result, named publication, or product mention may not function like a formal academic citation.

However, these signals still allocate visibility. They determine which sources, products, organizations, experts, countries, and domains are made visible to users.

MIBO therefore studies citation-like behavior as a machine information behavior, not as a direct equivalent of human scholarly citation.

## 7. Observation facility: MIBO

**MIBO — Machine Information Behavior Observatory** is the observation facility that operationalizes Machine Information Behavioral Sciences.

MIBO maintains:

- versioned query sets;
- repeated observations across AI systems;
- raw observation reports;
- metadata for each observation run;
- source-type and attribution taxonomies;
- public documentation for reproducibility.

MIBO began observation on **2026-05-05**.

## 8. Terminology

Use the following terms consistently:

| Concept | Preferred term |
|---|---|
| Parent field | Machine Behavioral Sciences |
| Specialized field | Machine Information Behavioral Sciences |
| Methodology | Longitudinal Machine Observation (LMO) |
| Facility | Machine Information Behavior Observatory (MIBO) |
| First research focus | source-attribution and citation-like behavior |
| Initial query collection | MIBO query set v0.1.0 |

Use US spelling: **Behavior / behavior**.

## 9. Scope boundaries

MIBO does not claim that machines have consciousness, intention, or agency in the human psychological sense.

MIBO does not claim that generative AI source display is identical to scholarly citation.

MIBO does not primarily optimize content for machine visibility. It observes and describes how machine systems allocate informational visibility.

## 10. One-sentence summary

> Machine Behavioral Sciences studies machines as observable behavioral entities; Machine Information Behavioral Sciences studies how those machines retrieve, select, attribute, recommend, omit, synthesize, transmit, and forget information; MIBO operationalizes this field through Longitudinal Machine Observation.
