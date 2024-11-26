import json
import pandas as pd

def import_json(file_path):
    with open(file_path,'r') as file:
        data_json = json.load(file)
    df = pd.DataFrame(data_json)
    # convert time to int
    df['time_s'].astype(int)
    return df
