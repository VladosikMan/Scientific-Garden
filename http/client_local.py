from http_client import Client_http 

class Client_local(Client_http):
    def __init__(self):
        pass

    def get_method(self, uri, params):
        print('google')