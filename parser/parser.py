import os
import PyPDF2
import pdfplumber

class Parser(object):
    def __init__(self):
        pass
# Тут есть ошибка , но пока хз как исправить. Функция просит два аргумента, но передавать надо один
    def search_files(folder,search_string):
        folder = "article"
        for file in os.listdir(folder):
            if file.endswith(".pdf"):
                file_path = os.path.join(folder, file)
                # Открываем и читаем файл
                try:
                    with pdfplumber.open(file_path) as pdf:
                        for page_idx, page in enumerate(pdf.pages):
                            text = page.extract_text()
                            if search_string.lower() in text.lower():
                                print(f"Файл: {file}, страница: {page_idx + 1}")
                except Exception as e:
                       print(f"Ошибка при чтении файла {file}: {e}")
