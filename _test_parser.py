import sys
sys.path.insert(0, r"c:\Users\admin\.cline\phishscope")
from phishscope.analyzer.email_parser import parse_eml

# Test with phishing sample
r = parse_eml(r"c:\Users\admin\.cline\phishscope\data\samples\phishing_sample.eml")
print("=== PHISHING SAMPLE ===")
print("URLs found:", r["urls"])
print("Attachments:", r["attachments"])
print("Plain body (first 80):", r["body_plain"][:80])
print("HTML body (first 80):", r["body_html"][:80])

# Test with legit sample
r2 = parse_eml(r"c:\Users\admin\.cline\phishscope\data\samples\legit_sample.eml")
print("\n=== LEGIT SAMPLE ===")
print("URLs found:", r2["urls"])
print("Attachments:", r2["attachments"])
print("Plain body (first 80):", r2["body_plain"][:80])
print("HTML body (first 80):", r2["body_html"][:80])