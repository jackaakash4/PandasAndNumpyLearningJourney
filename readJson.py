#read json file with pandas
import pandas as pd
import json

#using pd.read_json() to read JSON files in panda

data = {"One": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
        "Two": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102}}

json_data = json.dumps(data)

df_normalize = pd.json_normalize(json.loads(json_data))

#we can convert json into structured dataframes

df = pd.DataFrame(df_normalize)
print(df)
