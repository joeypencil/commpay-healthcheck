import requests
from . import constants


class APIManager:

    def __init__(self):
        self.payload = dict()
        self.headers = dict()
        self.response = None
    
    def is_last_api_call_ok(self) -> bool:
        if self.response.status_code == requests.codes.ok:
            return True
        else:
            return False
        
    def get_response_as_list(self) -> list:
        return self.response.json()
    
    def get_response_as_raw(self) -> str:
        return self.response.text

    def get_commpay_sites_data(self) -> None:
        self.response = requests.request('GET', constants.API_URL_SITES, 
            headers=self.headers, data=self.payload)
        
    def get_commpay_healthcheck_for_site(self, site: str) -> None:
        self.response = requests.request('GET', f'{site}{constants.API_ENDPOINT_HEALTHCHECK}', 
            headers=self.headers, data=self.payload)