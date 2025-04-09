import json
import pandas as pd

with open("029_data.json", "r") as file:
    data = json.load(file)

data= pd.json_normalize(data)

data.to_excel("031_data.xlsx", index=False)

print ("file created successfully: 031_data.xlsx")
