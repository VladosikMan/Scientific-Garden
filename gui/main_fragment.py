import sys
sys.path.insert(0, 'http')
sys.path.insert(1, 'data')
sys.path.insert(2, 'parser')

import webbrowser
import urllib.request
import customtkinter 
from constants import Constants
from app_client import App_http_client
from api_json import Scientific_api
from pars import Parser

class Article_fragment(customtkinter.CTk):
 
    def __init__(self, url):
        super().__init__()
      
        self.title("Фрагмент")
        self.geometry("400x300")
        self.url = url
        print(url)
        self.author_label = customtkinter.CTkLabel(self,text="Автор")  
        self.author_entry = customtkinter.CTkEntry(self)   
        self.author_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")  
        self.author_entry.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")  

        self.title_label = customtkinter.CTkLabel(self,text="Название статье")  
        self.title_entry = customtkinter.CTkEntry(self)   
        self.title_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")  
        self.title_entry.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="w") 

        self.data_label = customtkinter.CTkLabel(self,text="Дата 12.06.23")  
        self.data_entry = customtkinter.CTkEntry(self)   
        self.data_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")  
        self.data_entry.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="w") 


        self.h_label = customtkinter.CTkLabel(self,text="Индекс Хирша")  
        self.h_entry = customtkinter.CTkEntry(self)   
        self.h_label.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")  
        self.h_entry.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="w") 


        self.cancel_button = customtkinter.CTkButton(self, text="Отменить", command=self.destroy_fragment)
        self.save_button = customtkinter.CTkButton(self, text="Сохранить", command=self.save_article)
        self.cancel_button.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")  
        self.save_button.grid(row=4, column=1, padx=10, pady=(10, 0), sticky="w") 

    
    def save_article(self):
        parser.df.loc[len(parser.df.index )] = [self.author_entry.get(),self.title_entry.get(),self.data_entry.get(),self.h_entry.get()]
        print(parser.df)
        webbrowser.open(self.url,1)
        urllib.request.urlretrieve(self.url, f"article/{self.title_entry.get()}.pdf")
        self.destroy()
        pass

    def destroy_fragment(self):
    
        self.destroy()
        pass


class Element_frame(customtkinter.CTkFrame):
    def __init__(self, master, value):
        super().__init__(master, bg_color="yellow")
        self.grid_columnconfigure(0)
        print(value.title)
        
        self.article_title = customtkinter.CTkLabel(self, text=value.title,text_color="yellow", font=("Courier", 16))   
        self.type = customtkinter.CTkLabel(self,text=value.type)
        self.authors = customtkinter.CTkLabel(self,text=value.authors)
       
        self.link = customtkinter.CTkLabel(self,text=value.link)

        self.link.bind("<Button-1>", function_kek)
        self.summary = customtkinter.CTkTextbox(self,width=600)
        
        self.summary.insert("1.0", value.summary, None)
        
        self.article_title.grid(row=0, column=0, sticky="w")
        self.type.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.authors.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        self.link.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")
        self.summary.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")
        
def function_kek(event):
        #label_text = event.widget.cget("text")
        #print(label_text)
        #webbrowser.open(label_text,1)
        #urllib.request.urlretrieve(label_text, "file.pdf")
        create_window(event.widget.cget("text"))
        pass

def create_window(url):
    article_fragment = Article_fragment(url)
    article_fragment.mainloop()
    pass


class Settings_frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="yellow")

        self.buttont = customtkinter.CTkButton(self, text="Выход")
        self.buttont.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")


class  Search_line_frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="blue")
        
        self.grid_columnconfigure(0, weight=8)
        self.grid_columnconfigure(0, weight=2)
        self.grid_rowconfigure(0, weight=1)
        self.edit_request = customtkinter.CTkEntry(self, height=20)
        self.edit_request.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="we")
        self.buttont_request= customtkinter.CTkButton(self, text="Поиск", command=master.search_line_get)
        self.buttont_request.grid(row=0, column=1, padx=10, pady=(10, 0))
    

#список элементов
class List_result_frame(customtkinter.CTkScrollableFrame):
    def __init__(self, master,title, values):
        super().__init__(master, bg_color="green")
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            element_frame = Element_frame(self, value)
            element_frame.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="nsew")
            self.checkboxes.append(element_frame)


class  Params_frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="red")
        
        self.label_google = customtkinter.CTkLabel(self, text="Google API parameters")
        self.label_google.grid(row=0, column=0, padx=10, pady=(10, 0))

        self.label_1= customtkinter.CTkLabel(self, text="Года")
        self.label_1.grid(row=1, column=0, padx=10, pady=(10, 0))
        self.entry_year_1= customtkinter.CTkEntry(self)
        self.entry_year_1.grid(row=2, column=0)
        self.entry_year_2= customtkinter.CTkEntry(self)
        self.entry_year_2.grid(row=2, column=1)


class  Main_frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="white")

        self.grid_columnconfigure(0, weight=99)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=99)
        self.grid_rowconfigure(1, weight=1)

        l = []
        self.list_result_frame = List_result_frame(self, title="Element", values=l)
        self.params_frame = Params_frame(self)
        self.search_line_frame = Search_line_frame(self)

        self.list_result_frame.grid(row=0, column=0,  sticky="nsew")
        self.params_frame.grid(row=0, column=1, sticky="nsew")
        self.search_line_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)
    
    def search_line_get(self):
        print(self.search_line_frame.edit_request.get())
        if(self.search_line_frame.edit_request.get()!=""):

            params = {
                 "engine": "google_scholar",
                   "q": self.search_line_frame.edit_request.get(),
                   "api_key": "52060e9b662f6e470813ce9b9e689caa8d32e5d930b15ac042452c66baea664b",
                   "as_ylo": self.params_frame.entry_year_1.get(),
                   "as_yhi": self.params_frame.entry_year_2.get()
                   }
            result = self.master.app_client.get_google_request(params)
            self.update_list(result)

    def update_list(self,result):

        list_value = Scientific_api.convert_google_to_scientific_api(result)
        #print(len(list_value))
        self.list_result_frame.destroy

        self.list_result_frame = List_result_frame(self, title="Element", values=list_value)
        self.list_result_frame.grid(row=0, column=0,  sticky="nsew")

        pass



class Main_fragment_gui(customtkinter.CTk):
 
    def __init__(self):
        super().__init__()
        self.constants = Constants() 



        self.app_client = App_http_client()  
        self.title(self.constants.name_application)
        self.geometry("1280x720")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=9)
        self.grid_rowconfigure(0, weight=1)

        
        self.checkbox_frame = customtkinter.CTkFrame(self, bg_color="yellow")

        self.settings_frame = Settings_frame(self)
        self.main_frame = Main_frame(self)

        self.settings_frame.grid(row=0, column=0, sticky = "nsew")
        self.main_frame.grid(row=0, column=1,sticky="nsew")
 
   
parser = Parser()
print(parser.df)