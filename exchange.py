import pandas as pd
import requests
import json

df = pd.read_html("https://www.cbr.ru/eng/currency_base/daily/")
data = df[0]
data = data.rename(columns={"Num сode":"Num Code","Char сode":"Char Code", "Rate":"Rate"}) # I renamed columns because it does not work otherwise
data = data.to_dict(orient="records")
for i in data:
    if i["Char Code"]=="USD":
        print(i["Rate"])