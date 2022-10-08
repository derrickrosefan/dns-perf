import json
from qoe_data import QoeData

public_dns_results = QoeData()
local_dns_results = QoeData()

LOCAL_DNS_JSON_PATH = "./local_dns.json"
PUBLIC_DNS_JSON_PATH = "./local_dns.json"
LOCAL_DNS_CSV_PATH = "./local_dns.csv"
PUBLIC_DNS_CSV_PATH = "./public_dns.csv"

with open(LOCAL_DNS_JSON_PATH) as f:
    local_dns_data = json.load(f)
    for hostname, end_to_end_times in local_dns_data.items():
        for end_to_end_time in end_to_end_times:
            local_dns_results.add_data(
                {"hostname": hostname, "end_to_end_time": end_to_end_time}
            )
local_dns_results.save_data_to_csv(LOCAL_DNS_CSV_PATH)

with open(PUBLIC_DNS_JSON_PATH) as f:
    public_dns_data = json.load(f)
    for hostname, end_to_end_times in public_dns_data.items():
        for end_to_end_time in end_to_end_times:
            public_dns_results.add_data(
                {"hostname": hostname, "end_to_end_time": end_to_end_time}
            )
public_dns_results.save_data_to_csv(PUBLIC_DNS_CSV_PATH)
