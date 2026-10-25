# PhishScope - Email Phishing Analysis Pipeline

## Overview
PhishScope is an end-to-end email phishing analysis pipeline that parses `.eml` files, extracts Indicators of Compromise (IOCs), calculates risk scores, and generates comprehensive JSON reports with explainable text summaries.

## Architecture Diagram

```
+---------------------+      +---------------------+      +---------------------+
|  .eml File Input     | ---> |   Email Parser      | ---> |   IOC Extractor     |
+---------------------+      +---------------------+      +---------------------+
           |                       |                           |
           v                       v                           v
+---------------------+      +---------------------+      +---------------------+
|   Risk Scorer       | ---> |   Report Generator  | ---> |   JSON Report + Text  |
|   (Heuristic Rules) |      |   (Summary + JSON)  |      |   Summary Output    |
+---------------------+      +---------------------+      +---------------------+

                         |
                         v
                +---------------------+
                |     CLI Interface   |
                | (argparse subcommands) |
                +---------------------+
```

## Installation

```bash
# Clone and install dependencies
git clone <repository>
cd phishscope
pip install -r requirements.txt
```

## Requirements

```text
# Core dependencies (stdlib + minimal third-party)
certifi          # TLS/SSL verification for API calls
charset-normalizer # Character encoding detection
idna             # Internationalized domain name handling
rich             # Enhanced terminal output (for CLI summaries)
```

## Usage

### CLI Entry Point

```bash
# Analyze an .eml file (default output: report.json in CWD)
python -m phishscope.cli.main analyze data/samples/phishing_sample.eml

# Analyze with custom output path
python -m phishscope.cli.main analyze data/samples/phishing_sample.eml --output my_report.json
```

### Programmatic API

```python
from phishscope.analyzer.report import generate_report_from_eml

report = generate_report_from_eml("path/to/email.eml")
print(f"Risk Score: {report['risk_score']['total_score']}")
print(f"Risk Level: {report['risk_score']['risk_level']}")
```

### Output Example

```json
{
  "generated_at": "2024-01-15T10:30:45Z",
  "email": {
    "subject": "URGENT: Action Required - Account Suspended",
    "from": "support@paypal-security.com",
    "date": "2024-01-15T08:15:00Z"
  },
  "iocs": {
    "urls": ["http:// paypal-verify.com/login", "http:// 10.0.0.98/script.js"],
    "ips": ["10.0.0.98"],
    "domains": ["paypal-verify.com"],
    "hashes": {"sha256": ["a1b2c3d4..."], "md5": ["e5f6g7h8..."]}
  },
  "risk_score": {
    "total_score": 72,
    "risk_level": "HIGH",
    "breakdown": {
      "total": 72,
      "ip_in_url": 30,
      "at_in_url": 25,
      "spoofed_domain": 20,
      "urgency_keywords": 15,
      "suspicious_attachment": 10,
      "sender_mismatch": 5
    }
  },
  "email_bodies": {
    "plain": "Dear customer, your account will be suspended...",
    "html": "<html><body>Dear customer, your account will be suspended...</body></html>"
  },
  "attachments": []
}
```

## Sample Files

| File | Description |
|------|-------------|
| `data/samples/legit_sample.eml` | Legitimate business email (low risk) |
| `data/samples/phishing_sample.eml` | Phishing email with spoofed domain & urgent language (high risk) |

Run the end-to-end test:

```bash
python -m phishscope.cli.main analyze data/samples/phishing_sample.eml
```

Expected output:
```
Risk Score: 72
Risk Level: HIGH
Report saved to: data/samples/phishing_sample_report.json
```

## Development

### Running Tests

```bash
python -m pytest phishscope/tests/
```

### Adding New Sample EML Files

Place `.eml` files in `data/samples/` and ensure they follow standard MIME email format.

## License

MIT License - see LICENSE file for details.