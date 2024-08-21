import pandas as pd
import numpy as np
import os

class data_concat():
    def __init__(self, path, column_name):
        self.path = path
        self.column_name = column_name

    def concat(self):
        data_list = os.listdir(self.path)
        df_list = pd.DataFrame(columns = self.column_name)
        for data in data_list:
            df = pd.read_csv(os.path.join(self.path, data))
            df = df.query('순위 <= 25')
            df_list = pd.concat([df_list, df])
        return df_list