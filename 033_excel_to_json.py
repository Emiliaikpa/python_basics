import pandas as pd

my_file = pd.read_excel("032_books.xlsx")

my_file.to_json("034_data.json", orient="records", indent=4)
