# Week 1 Day 4 — AI Security Telemetry Pipeline

## Objective

Learn file handling, JSON, CSV, data parsing,
and structured security reporting.

## Project

AI Security Telemetry Pipeline.

## Pipeline

Raw Prompt File
→ Parsing
→ Normalization
→ Detection
→ Risk Scoring
→ Policy Decision
→ JSON Results
→ Human-Readable Report

## Outputs

- scan_results.json
- security_summary.json
- security_report.txt
- security_findings.csv

## Security Lessons

- Data formats do not imply trust.
- Security systems must handle failure states.
- "Scan failed" is different from "nothing suspicious found."
- Structured telemetry improves auditability.
- Security decisions need evidence.

## Limitations

Detection logic is intentionally basic and is
not a production prompt-injection defense.
