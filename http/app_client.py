from http_client_google import Client_http_google
import httpx


class App_http_client(object):
      def __init__(self):
        self.client_google = Client_http_google()
        
      
      def get_google_request(self,params):
        return self.client_google.get_method(params=params)