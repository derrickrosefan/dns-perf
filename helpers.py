import subprocess
import re

def get_ip_address_and_dns_query_time(hostname, dns_target):
    output = subprocess.check_output(
        [f"dig @{dns_target} {hostname} +noall +answer +stats"], shell=True,
    ).decode()
    print(hostname, "@", dns_target)
    ip_address = re.search(r"([0-9]{1,3}\.){3}[0-9]{1,3}$", output, re.MULTILINE).group(
        0
    )
    print(ip_address)
    query_time = re.search(
        "[0-9]+", re.search(r"Query time: [0-9]+ msec", output).group(0)
    ).group(0)
    print(query_time)
    return (ip_address, query_time)