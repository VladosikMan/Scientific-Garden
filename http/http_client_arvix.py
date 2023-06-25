from http_client import Client_http
import httpx
class Client_http_arvix(Client_http):
    def __init__(self):
        pass

    def get_method(self, uri, params):
        search = httpx.get(uri, params=params)
        results = search.content
        print(results)
