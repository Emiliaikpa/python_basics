import json
import pandas as pd

with open("035_signup_data.json", "r") as file:
    data = json.load(file)

data = pd.json_normalize(data)

data.to_excel("038_first_exam_result.xlsx", index=False)

print("file created successfully: 038_first_exam_result.xlsx")
