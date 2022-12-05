import logging
import pandas as pd


from bankruptcy_estates import BankruptcyEstate
from get_response import ResponseRetrieval
from datetime import datetime


def main():
    from_date = "2022-09-01"
    to_date = datetime.today().strftime("%Y-%m-%d")
    page_number = 0
    excel_file_name = f"bancrupcy_from{from_date}_to_{to_date}.xlsx"

    response = ResponseRetrieval(from_date=from_date, to_date=to_date, page_number=page_number)
    response, status_code =  response.get_response()
    response_in_json = response.json()


    retrieved_data = []

    while status_code == 200 and len(response_in_json["results"]) != 0:
        
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
                break

        page_number+=1
        response = ResponseRetrieval(from_date=from_date, to_date=to_date, page_number=page_number)
        response, status_code =  response.get_response()
        response_in_json = response.json()
        print(page_number)

    df = pd.DataFrame.from_dict(retrieved_data)

    with pd.ExcelWriter(excel_file_name, mode="w") as writer:
        df.to_excel(writer,sheet_name='Sheet1', index=False)

if __name__ == "__main__":
    main()
