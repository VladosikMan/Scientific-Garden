class Scientific_api(object):
    def __init__(self):
        # дата класс описания общего апи, информация общая для каждого ресурса, когда переход на отдельный файл
        self.title = "Заголовок"
        self.summary = "Описание"
        self.authors = "Авторы"
        self.type = "Тип"
        self.link = "Ссылка"
        #convert_google_to_scientific_apiself.data 
        
    
    @staticmethod
    def convert_google_to_scientific_api(result):
        list_api = []
        for i, value in enumerate(result):
            #print(value)
            sc_api = Scientific_api()
            try:
                sc_api.title = value['title']
            except Exception:
                pass
            try:
                sc_api.authors = value['publication_info']
            except Exception:
                pass
            try:
                sc_api.link = value['link']
            except Exception:
                pass
            try:
                sc_api.type = value['type']
            except Exception:
                pass

            try:
                sc_api.summary = value['snippet']
            except Exception:
                pass
        
            list_api.append(sc_api)
        
        print(len(list_api))
        print("ГРутьс")
        return list_api
        
