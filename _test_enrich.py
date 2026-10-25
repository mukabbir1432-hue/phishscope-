import sys
sys.path.insert(0, r"c:\Users\admin\.cline\phishscope")

from phishscope.api.clients.virustotal_client import enrich as vt_enrich
from phishscope.api.clients.urlscan_client import enrich as urlscan_enrich
from phishscope.api.clients.abuseipdb_client import enrich as abuseipdb_enrich

# Test VirusTotal client
vt_result = vt_enrich({"type": "url", "value": "http://secure-bank-verify.net/verify"})
print("=== VirusTotal ===")
print(vt_result)

# Test URLScan client
urlscan_result = urlscan_enrich({"type": "url", "value": "http://secure-bank-verify.net/verify"})
print("\n=== URLScan ===")
print(urlscan_result)

# Test AbuseIPDB client
abuseipdb_result = abuseipdb_enrich({"type": "ip", "value": "1.2.3.4"})
print("\n=== AbuseIPDB ===")
print(abuseipdb_result)