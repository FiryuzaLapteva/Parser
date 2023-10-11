import threading
import requests
import csv
import re

from modif_file import url_mod
url_mod('ru.txt', 'modified_urls.txt')

# Чтение URL адресов из файла
with open('modified_urls.txt', 'r', encoding='utf-8') as file:
    urls = [line.strip() for line in file]
#    print("Read URLs from file:", urls)

class Parser(threading.Thread):
   # Класс парсера
    def __init__(self, url, lock):
        threading.Thread.__init__(self)
        self.url = url
        self.lock = lock

    def run(self):
        try:
            response = requests.get(self.url, timeout=5, auth=('user', 'pass'))
            if response.status_code == 200:
                content = response.content.decode('utf-8') 
                russian_pattern = re.compile(r'[а-яА-ЯёЁ]+')# оставляем только русские симловы
                russian_words = russian_pattern.findall(content)# Применяем фильтрацию по русским словам к контенту
                russian_text = ' '.join(russian_words) # объединяем слова через пробел
            # Пройтись по распарсенным данным и записать каждую строку
                with self.lock:
                    with open('parsed_data.csv', mode='a', newline='', encoding='utf-8') as file:
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([self.url, russian_text])
            else:
                print(f'Произошла ошибка при выполнении запроса для URL: {self.url}')
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при запросе для URL: {self.url}, {e}')
          
# Создаем объект блокировки
lock = threading.Lock()

# Создаем и запускаем обработчики
threads = []
for url in urls[5001:6000]:
    parser = Parser(url, lock)
    parser.start()
    threads.append(parser)

# Ожидаем завершения всех обработчиков
for parser in threads:
    parser.join()

# Создайте строку заголовка для CSV-файла (если необходимо)
#header = ['url', 'content']

# Откройте CSV-файл в режиме записи и запишите заголовок
#with open('parsed_data.csv', mode='w', newline='', encoding='utf-8') as file:
    #csv_writer = csv.writer(file, quotechar='', quoting=csv.QUOTE_NONE)
   
