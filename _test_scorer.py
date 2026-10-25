import sys
sys.path.insert(0, r"c:\Users\admin\.cline\phishscope")

from phishscope.analyzer.email_parser import parse_eml
from phishscope.analyzer.ioc_extractor import extract_urls, extract_ips, extract_domains, extract_hashes
from phishscope.analyzer.risk_scorer import score_email

# Test with phishing sample
r = parse_eml(r"c:\Users\admin\.cline\phishscope\data\samples\phishing_sample.eml")
iocs = {
    "urls": extract_urls(r["body_plain"] + " " + r["body_html"]),
    "ips": extract_ips(r["body_plain"] + " " + r["body_html"]),
    "domains": extract_domains(r["body_plain"] + " " + r["body_html"]),
}

result = score_email(r, iocs)
print("=== PHISHING SAMPLE ===")
print("IOCs - URLs:", iocs["urls"])
print("IOCs - IPs:", iocs["ips"])
print("IOCs - Domains:", iocs["domains"])
print("Score:", result["score"])
print("Risk Level:", result["risk_level"])

# Test with legit sample
r2 = parse_eml(r"c:\Users\admin\.cline\phishscope\data\samples\legit_sample.eml")
iocs2 = {
    "urls": extract_urls(r2["body_plain"] + " " + r2["body_html"]),
    "ips": extract_ips(r2["body_plain"] + " " + r2["body_html"]),
    "domains": extract_domains(r2["body_plain"] + " " + r2["body_html"]),
}

result2 = score_email(r2, iocs2)
print("\n=== LEGIT SAMPLE ===")
print("IOCs - URLs:", iocs2["urls"])
print("IOCs - IPs:", iocs2["ips"])
print("IOCs - Domains:", iocs2["domains"])
print("Score:", result2["score"])
print("Risk Level:", result2["risk_level"])