import requests

class ResponseRetrieval:
    def __init__(self, from_date, to_date, page_number=0):
        self.from_date = from_date
        self.to_date = to_date
        self.page_number = page_number
        self._url = f"https://www.statstidende.dk/api/messagesearch?d=false&fromDate={self.from_date}T00:00:00&m=603102f09e3f5ad99538175719970bde&m=14a1d71df21558e5ade0214f90482cdc&m=24295ca1259a5876ba7bf8ef496feed6&m=383f18001b395f39825061a5c0798fad&m=018d01410efb5472a6989328817df00a&m=941c2e759f325408a946031217b6d669&messageloguser=&o=40&page={self.page_number}&ps=100&teamsOnly=false&toDate={self.to_date}T00:00:00&userOnly=false"

    def get_response(self):
        response = requests.get(self._url, verify=False)
        return response, response.status_code