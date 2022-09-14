import requests

class ResponseRetrieval:
    def __init__(self, from_date, to_date, page_number=0):
        self.from_date = from_date
        self.to_date = to_date
        self.page_number = page_number
        self._url = f"https://www.statstidende.dk/api/messagesearch?d=false&fromDate={self.from_date}T00:00:00&m=14a1d71df21558e5ade0214f90482cdc&messageloguser=&o=40&page={self.page_number}&ps=10&teamsOnly=false&toDate={self.to_date}T00:00:00&userOnly=false"

    def get_response(self):
        response = requests.get(self._url, verify=False)
        return response, response.status_code
