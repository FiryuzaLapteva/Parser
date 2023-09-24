import threading
from threading import Thread
import requests
from bs4 import BeautifulSoup
import json

class Parser(Thread):
    """ Класс парсера """
 
    def __init__(self, url, lock):
        Thread.__init__(self)
        self.url = url
        self.lock = lock

    def run(self):
        """ Запуск обработки """
        response = requests.get(self.url)
        with self.lock:
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                soup = soup.find_all('h1', class_='headline-1')
                print('Запрос выполнен успешно')
                # Добавить заголовки в лист
                all_article_titles = []
                article_titles = [inner.text for inner in soup]
                all_article_titles.extend(article_titles)
                # записать все заголовки в файл
                with open('spider_file.json', 'w', encoding='utf-8') as file:
                    json.dump(all_article_titles, file, ensure_ascii=False, indent=4)
            else:
                print('Произошла ошибка при выполнении запроса')
    

# Список URL-адресов для парсинга
urls = ['https://holdings.panasonic', 'https://nic.panasonic']

# Создаем объект блокировки
lock = threading.Lock()

# Создаем и запускаем обработчики
threads = []
for url in urls:
    parser = Parser(url, lock)
    parser.start()
    threads.append(parser)
 
# Ожидаем завершения всех обработчиков
for parser in threads:
    parser.join()