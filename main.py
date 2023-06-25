import sys
sys.path.insert(0, 'http')

from http_client import Client_http
from http_client_google import Client_http_google
from client_local import Client_local 

def main():
	print("Дайте печенье.")
	google_client = Client_http_google()
	params = {
		"engine": "google_scholar",
		"q": "coffe",
	    "api_key": "52060e9b662f6e470813ce9b9e689caa8d32e5d930b15ac042452c66baea664b"
    }
	uri = ""
	google_client.get_method(uri, params)
	
main()