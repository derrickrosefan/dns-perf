import pandas as pd
from helpers import get_ip_address_and_dns_query_time

HOSTNAMES = [
    "google.com",
    "youtube.com",
    "facebook.com",
    "amazon.com",
    "yahoo.com",
    "twitter.com",
    "instagram.com",
    "wikipedia.com",
    "reddit.com",
    "discord.com",
]
PUBLIC_DNS = "8.8.8.8"
LOCAL_DNS = "1.1.1.1"

public_dns_results = pd.DataFrame({"hostname": [], "query_time": [], "ip_address": []})
local_dns_results = pd.DataFrame({"hostname": [], "query_time": [], "ip_address": []})

for hostname in HOSTNAMES:
    (public_dns_ip_address, public_dns_query_time) = get_ip_address_and_dns_query_time(
        hostname, PUBLIC_DNS
    )
    public_dns_results.loc[len(public_dns_results.index)] = [
        hostname,
        int(public_dns_query_time),
        public_dns_ip_address,
    ]
    (local_dns_ip_address, local_dns_query_time) = get_ip_address_and_dns_query_time(
        hostname, LOCAL_DNS
    )
    local_dns_results.loc[len(local_dns_results.index)] = [
        hostname,
        int(local_dns_query_time),
        local_dns_ip_address,
    ]
print(public_dns_results)
print(local_dns_results)
