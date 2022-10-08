import pandas as pd

class QoeData:
    def __init__(self):
        self.data = pd.DataFrame({"hostname": [], "end_to_end_time": []})

    def add_data(self, data):
        try:
            self.data.loc[len(self.data.index)] = data
        except:
            print("Malformed data", data)

    def save_data_to_csv(self, path):
        self.data.to_csv(path)
