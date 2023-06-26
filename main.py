import sys
sys.path.insert(0, 'http')
sys.path.insert(1, 'gui')
sys.path.insert(2, 'parser')

from http_client import Client_http
from http_client_google import Client_http_google
from http_client_arvix import Client_http_arvix
from client_local import Client_local 
from main_fragment import Main_fragment_gui
from parser import Parser

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

def test_arvix():
    print("Дайте arvix.")
    arvix_client = Client_http_arvix()
    url_arvix = 'http://export.arxiv.org/api/query'
    arvix_params = {
        'search_query': 'all:"machine learning" OR all:"deep learning"',
        'start': 0, 
        'max_results': 10
    }
    arvix_client.get_method(url_arvix, arvix_params)

def start_gui():
	main_fragment_gui = Main_fragment_gui()

def test_parcer():
    parser = Parser()
    folder = "article"
    search_string = "INTRODUCTION" 
    parser.search_files(search_string)

#main()
#test_arvix()
#start_gui()
test_parcer()
