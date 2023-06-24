from http_client import Client_http

class Client_http_google(Client_http):
    def __init__(self):
        pass

    def get_method(self, uri, data):
        print('google')