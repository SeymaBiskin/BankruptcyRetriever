import os.path
import logging
import pandas as pd


from bankruptcy_estates import BankruptcyEstate
from get_response import ResponseRetrieval
from datetime import datetime

excel_file_name = "run1.xlsx"
path_to_excel_file = f"{os.getcwd()}\{excel_file_name}" 

# to_date = datetime.today().strftime("%Y-%m-%d")
to_date = "2022-03-01"
from_date = "2021-09-01"
page_number = 0

response = ResponseRetrieval(from_date=from_date, to_date=to_date, page_number=page_number)
response, status_code =  response.get_response()
response_in_json = response.json()

retrieved_data = []

while status_code == 200 and response_in_json["resultCount"] != 0:
    
    for data in response_in_json["results"]:
        try:
            bankruptcy_estates = BankruptcyEstate(message_number=data["messageNumber"],
                                                bankruptcy_estate=data["title"],
                                                cvr_no=data["summary"][0]["value"],
                                                court_district=data["summary"][1]["value"],
                                                publish_date=data["published"])
            retrieved_data.append(bankruptcy_estates.get_as_dict())                                
        except Exception as e:
            logging.exception(e)
            bankruptcy_estates = BankruptcyEstate(bankruptcy_estate=data["title"])
            retrieved_data.append(bankruptcy_estates.get_as_dict())   
            continue

    page_number+=1
    response = ResponseRetrieval(from_date=from_date, to_date=to_date, page_number=page_number)
    response, status_code =  response.get_response()
    response_in_json = response.json()

df = pd.DataFrame.from_dict(retrieved_data)

with pd.ExcelWriter(excel_file_name, mode="w") as writer:
    df.to_excel(writer,sheet_name='Sheet1', index=False)


