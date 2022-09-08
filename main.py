
from operator import index
from statistics import mode
import requests
import pandas as pd
import openpyxl
import os.path


from datetime import datetime

from_date = "2022-01-01"
to_date = datetime.today().strftime("%Y-%m-%d")
page_number = 0
url = f"https://www.statstidende.dk/api/messagesearch?d=false&fromDate={from_date}T00:00:00&m=603102f09e3f5ad99538175719970bde&m=14a1d71df21558e5ade0214f90482cdc&m=24295ca1259a5876ba7bf8ef496feed6&m=383f18001b395f39825061a5c0798fad&m=018d01410efb5472a6989328817df00a&m=941c2e759f325408a946031217b6d669&messageloguser=&o=40&page={page_number}&ps=100&teamsOnly=false&toDate={to_date}T00:00:00&userOnly=false"
excel_file_name = "test.xlsx"      

response = requests.get(url, verify=False)
response_in_json =  response.json()


retrieved_data = {}
for data in response_in_json["results"]:
    retrieved_data["MessageNumber"] = [data["messageNumber"]]
    retrieved_data["BankruptcyEstate"] = [data["title"]]
    retrieved_data["CVRNo"] = [data["summary"][0]["value"]]
    retrieved_data["CourtDistrict"] = [data["summary"][1]["value"]]

    print(retrieved_data)

    break

df = pd.DataFrame.from_dict(retrieved_data)

path_to_excel_file = f"{os.getcwd()}\{excel_file_name}"




with pd.ExcelWriter(excel_file_name, mode="w") as writer:
    df.to_excel(writer,sheet_name='Sheet1')


