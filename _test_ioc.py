import sys
sys.path.insert(0, r"c:\Users\admin\.cline\phishscope")

from phishscope.analyzer.email_parser import parse_eml
from phishscope.analyzer.ioc_extractor import extract_urls, extract_ips, extract_domains, extract_hashes

# Test with phishing sample
r = parse_eml(r"c:\Users\admin\.cline\phishscope\data\samples\phishing_sample.eml")
print("=== PHISHING SAMPLE IOC EXTRACTION ===")
print("URLs:", extract_urls(r["body_plain"] + " " + r["body_html"]))
print("IPs:", extract_ips(r["body_plain"] + " " + r["body_html"]))
print("Domains:", extract_domains(r["body_plain"] + " " + r["body_html"]))
print("Hashes:", extract_hashes(r["attachments"]))

# Test with legit sample
r2 = parse_eml(r"c:\Users\admin\.cline\phishscope\data\samples\legit_sample.eml")
print("\n=== LEGIT SAMPLE IOC EXTRACTION ===")
print("URLs:", extract_urls(r2["body_plain"] + " " + r2["body_html"]))
print("IPs:", extract_ips(r2["body_plain"] + " " + r2["body_html"]))
print("Domains:", extract_domains(r2["body_plain"] + " " + r2["body_html"]))
print("Hashes:", extract_hashes(r2["attachments"]))