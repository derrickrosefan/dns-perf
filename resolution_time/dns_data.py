import pandas as pd


class DnsData:
    def __init__(self):
        self.data = pd.DataFrame({"hostname": [], "query_time": [], "ip_address": []})

    def add_data(self, data):
        try:
            self.data.loc[len(self.data.index)] = data
        except:
            print("Malformed data", data)

    def save_data_to_csv(self, path):
        self.data.to_csv(path)
