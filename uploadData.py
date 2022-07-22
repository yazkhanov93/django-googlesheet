import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import json
import pandas as pd
import  schedule
import time


scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
def get_info():
    creds = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)

    client = gspread.authorize(creds)

    sheet = client.open('Copy of test').sheet1

    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    df["стоимость в руб"] = df["стоимость,$"] * 1
    # data = df.to_json(orient="records")
    print(df)

schedule.every(10).seconds.do(get_info)

while 1:
    schedule.run_pending()
    time.sleep(1)