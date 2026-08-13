#!/usr/bin/env python3
"""Validate the active historical scope and core archival structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "hierarchy.md",
    "laws.md",
    "AUDIT.md",
    "paper-b/README.md",
    "CITATION.cff",
    "LICENSE",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def validate_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    require(not missing, f"missing required files: {', '.join(missing)}")


def validate_citation() -> None:
    text = read("CITATION.cff")
    require("\t" not in text, "CITATION.cff must not contain tab indentation")
    required_patterns = {
        "cff-version": r"(?m)^cff-version:\s*1\.2\.0\s*$",
        "message": r"(?m)^message:\s*.+$",
        "title": r'(?m)^title:\s*["\']?MIBO Pilot Core["\']?\s*$',
        "type": r"(?m)^type:\s*(software|dataset)\s*$",
        "authors": r"(?m)^authors:\s*$",
        "family-names": r'(?m)^\s+- family-names:\s*["\']?Sasano["\']?\s*$',
        "given-names": r'(?m)^\s+given-names:\s*["\']?Kento["\']?\s*$',
        "affiliation": r'(?m)^\s+affiliation:\s*["\']?Okayama University["\']?\s*$',
        "repository-code": r"(?m)^repository-code:\s*[\"']?https://github\.com/mibo-research-pilot/core[\"']?\s*$",
        "license": r'(?m)^license:\s*["\']?Apache-2\.0["\']?\s*$',
    }
    for field, pattern in required_patterns.items():
        require(re.search(pattern, text) is not None, f"CITATION.cff missing or invalid field: {field}")
    forbidden = ("doi:", "identifiers:", "journal:", "date-released:")
    require(not any(token in text.lower() for token in forbidden), "CITATION.cff contains unsupported publication metadata")


def validate_readme() -> None:
    text = read("README.md")
    lower = text.lower()
    plain = text.replace("*", "")
    require("MIBO — Machine Information Behavioral Observatory" in text, "README missing official English name")
    require("機械情報行動観測所" in text, "README missing Japanese name")
    require("API-based continuously from Day 1" in text, "README missing API-from-Day-1 statement")
    require("Day 1–Day 13 / 244 included observations" in text, "README missing Paper B freeze boundary")
    require("Day 13 is not the end of the whole Pilot" in text, "README incorrectly leaves the Pilot ending ambiguous")
    require("not the authoritative repository" in plain, "README missing post-Pilot repository firewall")
    require("historical conceptual, methodological, and claim-development record" in lower, "README missing historical repository role")
    require("https://github.com/mibo-research-pilot/queries" in text, "README missing queries repository link")
    require("https://github.com/mibo-research-pilot/reports" in text, "README missing reports repository link")
    require("mibo-science/" not in text and "mibo-research/" not in text, "README contains a non-Pilot repository reference")
    require("does not claim conceptual priority" in text and "world's first" in lower, "README missing the priority-claim firewall")
    require("canonical-definitions-v0.1.md" not in text, "README contains the former broken canonical-definitions link")
    require("Apache License 2.0" in text and "CC0" not in text, "README license statement conflicts with LICENSE")


def validate_historical_documents() -> None:
    hierarchy = read("hierarchy.md")
    laws = read("laws.md")
    require("Historical MIBO Pilot Field and Terminology Development" in hierarchy, "hierarchy missing historical status")
    require("MIBO — Machine Information Behavioral Observatory" in hierarchy, "hierarchy missing current terminology mapping")
    require("Observation**, **Parallelism**, **Embedded openness**, and **Non-stationarity" in hierarchy, "hierarchy missing OPEN Principles")
    require("Historical MIBO Pilot Claim Registry" in laws, "laws.md missing historical registry title")
    disclaimer_parts = (
        "The term “Law” is historical MIBO Pilot terminology",
        "provisional, corrigible longitudinal claim",
        "not a universal law of nature",
        "a validated scale",
        "a causal law",
        "a confirmatory post-Pilot result",
    )
    for part in disclaimer_parts:
        require(part in laws, f"laws.md disclaimer missing: {part}")
    require("Historical Pilot gender coding" in laws, "laws.md missing gender-coding limitation")
    require("API-based continuously from Day 1" in laws, "laws.md missing corrected collection provenance")

    law_ids = re.findall(r"(?m)^### Law ([IVX]+)\b", laws)
    expected_laws = {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"}
    require(len(law_ids) == len(set(law_ids)), "duplicate Law headings found")
    require(set(law_ids) == expected_laws, "historical Law IDs changed or are missing")

    candidate_ids = [int(value) for value in re.findall(r"(?m)^### P(\d+)\b", laws)]
    require(len(candidate_ids) == len(set(candidate_ids)), "duplicate candidate headings found")
    require(set(candidate_ids) == set(range(12, 35)), "historical candidate IDs P12-P34 changed or are missing")


def validate_paper_b() -> None:
    text = read("paper-b/README.md")
    require("Operationalizing Longitudinal Machine Information Behavior: The Founding and Developmental Pilot of MIBO" in text, "Paper B title missing")
    require("Day 1–Day 13" in text and "244" in text, "Paper B boundary missing")
    require("not the end of the MIBO Pilot" in text, "Paper B file treats the freeze as the Pilot end")
    require("not contain the primary raw observation dataset" in text, "core/data role is ambiguous")
    require("https://github.com/mibo-research-pilot/queries" in text, "Paper B file missing queries link")
    require("https://github.com/mibo-research-pilot/reports" in text, "Paper B file missing reports link")


def validate_current_provenance() -> None:
    current_files = ("README.md", "paper-b/README.md")
    forbidden_claims = (
        "first api-collected session",
        "from day 14 the pilot collects via provider apis rather than the web interface",
    )
    for path in current_files:
        lower = read(path).lower()
        for claim in forbidden_claims:
            require(claim not in lower, f"{path} contains an unqualified false collection-transition claim")
    laws = read("laws.md").lower()
    require("day 14 (first api-collected session)" not in laws, "laws.md retains the false Day 14 collection claim")
    require(forbidden_claims[1] not in laws, "laws.md retains the false web-to-API transition claim")


def validate_local_links() -> None:
    for path in ("README.md", "AUDIT.md", "hierarchy.md", "laws.md", "paper-b/README.md"):
        text = read(path)
        for target in re.findall(r"\]\((\./[^)#]+)", text):
            resolved = ((ROOT / path).parent / target).resolve()
            require(resolved.is_file() or resolved.is_dir(), f"broken local link in {path}: {target}")


def main() -> int:
    checks = (
        ("required archival files", validate_required_files),
        ("CITATION.cff structure", validate_citation),
        ("README historical scope", validate_readme),
        ("hierarchy and claim registry", validate_historical_documents),
        ("Paper B boundary", validate_paper_b),
        ("API collection provenance", validate_current_provenance),
        ("local Markdown links", validate_local_links),
    )
    try:
        for label, check in checks:
            check()
            print(f"PASS: {label}")
    except (AssertionError, OSError, UnicodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
