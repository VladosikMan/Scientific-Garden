import sys
sys.path.insert(0, 'http')
sys.path.insert(1, 'gui')

from http_client import Client_http
from http_client_google import Client_http_google
from app_client import App_http_client
from client_local import Client_local 
from main_fragment import Main_fragment_gui
 

class App(object):
	def __init__(self):
		self.app_client = App_http_client()
		self.main_fragment_gui = Main_fragment_gui()
		self.main_fragment_gui.mainloop() 

app = App()