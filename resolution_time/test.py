from dns_data import DnsData
from constants import (
    HOSTNAMES,
    LOCAL_DNS_CSV_PATH,
    NUM_TRIALS_PER_HOSTNAME,
    PUBLIC_DNS,
    LOCAL_DNS,
    PUBLIC_DNS_CSV_PATH,
)
from dns_timer import get_ip_address_and_dns_query_time

public_dns_results = DnsData()
local_dns_results = DnsData()

for hostname in HOSTNAMES:
    for _ in range(NUM_TRIALS_PER_HOSTNAME):
        (
            public_dns_ip_address,
            public_dns_query_time,
        ) = get_ip_address_and_dns_query_time(hostname, PUBLIC_DNS)
        public_dns_results.add_data(
            {
                "hostname": hostname,
                "query_time": int(public_dns_query_time),
                "ip_address": public_dns_ip_address,
            }
        )
        (
            local_dns_ip_address,
            local_dns_query_time,
        ) = get_ip_address_and_dns_query_time(hostname, LOCAL_DNS)
        local_dns_results.add_data(
            {
                "hostname": hostname,
                "query_time": int(local_dns_query_time),
                "ip_address": local_dns_ip_address,
            }
        )
public_dns_results.save_data_to_csv(PUBLIC_DNS_CSV_PATH)
local_dns_results.save_data_to_csv(LOCAL_DNS_CSV_PATH)
