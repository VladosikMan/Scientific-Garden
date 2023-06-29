import os
import PyPDF2
import pdfplumber
import pandas as pd
import difflib
# Директория где хранятся данные 
folder = "./article/"
# Формат сатей
format_file = ".pdf"
# Коэффциент при котором запрос валиден 
norm_coeff = 0.60

class Parser(object):
    def __init__(self):
        pass
    # Основной словарь которы йдолжен обновлятся по мере скачивания записей с помощью парсера и заполнять вручную если статьи скачали сами
    df = pd.DataFrame({
        'author': ['AA', 'BB', 'AA', 'DD'],
        'name_article': ["asd", "asdf", "asdff", "asdfff"],
        'data': ["12.06.05", "12.04.54", "1.02.3", "12.312.21"],
        'h_index' :["1","2","3","4"]
    })
    
    # Проверка совпадения строк от 0.00 до 1.00
    def similarity(self, s1, s2):
      normalized1 = s1.lower()
      normalized2 = s2.lower()
      matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
      return matcher.ratio()
    
    # поиск строки по всем статьям
    def search_string(self,search_string):
        resf = pd.DataFrame({'file' : [], 'page' : []})
        for file in os.listdir(folder):
            if file.endswith(".pdf"):
                file_path = os.path.join(folder, file)
    
                # Открываем и читаем файл
                try:
                    with pdfplumber.open(file_path) as pdf:
                        for page_idx, page in enumerate(pdf.pages):
                            text = page.extract_text()
                            if search_string.lower() in text.lower():
                                resf.loc[ len(resf.index )] = [file, page_idx+1]
                                ##print(f"Файл: {file}, страница: {page_idx + 1}")
                except Exception as e:
                    print(f"Ошибка при чтении файла {file}: {e}")
        return resf                
    
    # Поиск по названию статьи
    def search_name_article(self, search_name):
        res = []
        for file in os.listdir(folder):
            coeff = self.similarity(file, search_name + format_file)
            if (coeff>norm_coeff):
                res.append(file)
        return res            
                
    
    # Поиск по категории
    def search_category(self, name_category, search_param):
        res = []
        for i, category in self.df[name_category].items():
            coeff = self.similarity(category, search_param)
            if(coeff > norm_coeff):
                name_article = (self.df.iloc[i]['name_article'])
                res.append(name_article + format_file)
    
        # Удаляем повторяющиеся элементы   
        temp = []
        [temp.append(x) for x in res if x not in temp]
        res = temp
        return res  
