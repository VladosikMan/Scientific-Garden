import customtkinter
from constants import Constants


class Settings_frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="yellow")

        self.buttont = customtkinter.CTkButton(self, text="checkbox 1")
        self.buttont.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.buttont2 = customtkinter.CTkButton(self, text="checkbox 2")
        self.buttont2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")


class  Search_line_frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="blue")
        
        self.buttont = customtkinter.CTkButton(self, text="checkbox 1")
        self.buttont.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.buttont2 = customtkinter.CTkButton(self, text="checkbox 2")
        self.buttont2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")


class  List_result_frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="green")
        
        self.buttont = customtkinter.CTkButton(self, text="checkbox 1")
        self.buttont.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.buttont2 = customtkinter.CTkButton(self, text="checkbox 2")
        self.buttont2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")


class  Params_frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="red")
        
        self.buttont = customtkinter.CTkButton(self, text="checkbox 1")
        self.buttont.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.buttont2 = customtkinter.CTkButton(self, text="checkbox 2")
        self.buttont2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")


class  Main_frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color="white")

        self.grid_columnconfigure(0, weight=7)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=95)
        self.grid_rowconfigure(1, weight=5)

        self.list_result_frame = List_result_frame(self)
        self.params_frame = Params_frame(self)
        self.search_line_frame = Search_line_frame(self)

        self.list_result_frame.grid(row=0, column=0,  sticky="nsew")
        self.params_frame.grid(row=0, column=1, sticky="nsew")
        self.search_line_frame.grid(row=1, column=0, sticky="nsew", columnspan=2)



class Main_fragment_gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.constants = Constants()
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

        ##self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
      ## self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")


app = Main_fragment_gui()
app.mainloop()
