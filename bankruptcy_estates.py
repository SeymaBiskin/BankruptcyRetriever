from dataclasses import dataclass, asdict

@dataclass
class BankruptcyEstate:
    message_number: str= "NA"
    bankruptcy_estate: str= "NA"
    cvr_no:str = "NA"
    court_district: str = "NA"

    def get_as_dict(self) -> dict:
        return asdict(self)

  





