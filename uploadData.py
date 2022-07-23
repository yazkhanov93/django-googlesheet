import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import json
import pandas as pd
import  schedule
import time


scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
def get_info():
    try:
        usd = None
        df = pd.read_html("https://www.cbr.ru/eng/currency_base/daily/")
        data = df[0]
        data = data.rename(columns={"Num сode":"Num Code","Char сode":"Char Code", "Rate":"Rate"}) # I renamed columns because it does not work otherwise
        data = data.to_dict(orient="records")
        for i in data:
            if i["Char Code"]=="USD":
                usd = i["Rate"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open('Copy of test').sheet1
        data = sheet.get_all_records()
        df = pd.DataFrame(data)
        df["стоимость в руб"] = df["стоимость,$"] * usd
        df = df.rename(columns={"№":"orderNumber","заказ №":"orderId", "стоимость,$":"priceUSD", "стоимость в руб":"priceRUB", "срок поставки":"deliveryTime"})
        data = df.to_dict(orient="records")
        json_data = json.dumps(data, ensure_ascii=False)
        upload = requests.post(url="http://127.0.0.1:8000/order-upload/", data=json_data, headers={'Content-Type': 'application/json; charest=utf-8'})
        print("uploaded")
    except:
        print("orders already exist or no internet connection")
    

schedule.every(10).seconds.do(get_info)

while 1:
    schedule.run_pending()
    time.sleep(1)