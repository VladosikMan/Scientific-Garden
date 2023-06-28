from http_client import Client_http
from serpapi import GoogleSearch


class Client_http_google(Client_http):
    def __init__(self):
        self.api_key = "52060e9b662f6e470813ce9b9e689caa8d32e5d930b15ac042452c66baea664b"
        pass

    def get_method(self, params):
        print('google')
        params['myapi_keynewkey'] = self.api_key
        #print(params)
        search = GoogleSearch(params)
        results = search.get_dict()
        #print(results)
        organic_results = results["organic_results"]
        #print(organic_results)
        return organic_results
        #print(organic_results[0])

        

#google_client = Client_http_google()
#params = {
#     "engine": "google_scholar",
#     "q": "МОДЕРНИЗАЦИЯ СИСТЕМ ЧПУ ДЛЯ МЕТАЛЛОРЕЖУЩЕГО ОБОРУДОВАНИЯ",
#   "api_key": "52060e9b662f6e470813ce9b9e689caa8d32e5d930b15ac042452c66baea664b"
#}
#uri = ""
#google_client.get_method(params)