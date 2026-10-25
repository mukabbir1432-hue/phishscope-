# PhishScope v1.0.0 - Project State

## Frozen Interface Contracts
- ParsedEmail: dataclass with fields for email parsing results
- IOCSet: collection of IOC objects
- EnrichmentResult: results from API enrichment
- RiskAssessment: scoring result with severity
- FiredRule: individual rule that fired with evidence
- ReportBundle: generated report in multiple formats

## File Manifest
| Path | Status |
|---|---|
| phishscope/__init__.py | pending |
| phishscope/analyzer/ | pending |
| phishscope/api_clients/ | pending |
| phishscope/data/ | pending |
| phishscope/reports/ | pending |
| phishscope/tests/ | pending |
| phishscope/web/ | pending |
| phishscope/.github/workflows/ | pending |
| phishscope/Makefile | pending |
| phishscope/Dockerfile | pending |
| phishscope/docker-compose.yml | pending |
| phishscope/.pre-commit-config.yaml | pending |
| phishscope/pyproject.toml | pending |
| phishscope/.env.example | pending |
| phishscope/main.py | pending |
| phishscope/benchmark.py | pending |

## Decisions Log
- **Python 3.11**: Exact version requirement everywhere
- **Cross-platform**: Windows 11 AND Ubuntu 22.04 support
- **Free-tier APIs only**: VirusTotal, URLScan, AbuseIPDB, WHOIS
- **Offline-first**: Parsing, IOC extraction, heuristics, scoring, reporting work offline
- **Internet only**: Enrichment layers (VT, URLScan, AbuseIPDB, WHOIS/DNS)
- **MIT License**: Version 1.0.0

## Open TODOs
- [ ] Create folder structure and __init__.py files
- [ ] Define data models (frozen pydantic/pydantic-less)
- [ ] Implement email parser (MIME, headers, bodies, attachments)
- [ ] Implement IOC extractor with Unicode normalization
- [ ] Implement domain intel (homoglyph, lookalike, WHOIS)
- [ ] Implement auth checks (SPF, DKIM, DMARC)
- [ ] Implement attachment forensics (hashing, macro detection, QR)
- [ ] Implement enricher with cached API clients
- [ ] Implement scorer with declarative rules
- [ ] Implement report generator (md, pdf, json)
- [ ] Implement CLI with subcommands
- [ ] Implement web UI with Flask
- [ ] Create sample .eml corpus
- [ ] Implement benchmark suite
- [ ] Set up CI/CD workflows
- [ ] Write documentation

## Current Part: 7