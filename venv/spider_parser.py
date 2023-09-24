import threading
import requests
from bs4 import BeautifulSoup
import json

class Parser(threading.Thread):
    """Класс парсера"""

    def __init__(self, url, lock):
        threading.Thread.__init__(self)
        self.url = url
        self.lock = lock

    def run(self):
        """Запуск обработки"""
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                soup = soup.find_all('h1', class_='headline-1')
                print(f'Запрос выполнен успешно для URL: {self.url}')
                # Добавить заголовки в лист
                all_article_titles = []
                article_titles = [inner.text for inner in soup]
                all_article_titles.extend(article_titles)
                # Записать все заголовки в файл
                with self.lock:
                    with open('spider_file.json', 'w', encoding='utf-8') as file:
                        json.dump(all_article_titles, file, ensure_ascii=False, indent=4)
                        file.write('\n')  # записывать данные с новой строки
            else:
                print(f'Произошла ошибка при выполнении запроса для URL: {self.url}')
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при запросе для URL: {self.url}, {e}')

    # определяем пути для исходных и изменных данных URLs
input_file_path = 'urls.txt'
output_file_path = 'modified_urls.txt'

# открываем исходный файл для чтения и изменный файл для записи
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Итеративно проходим по каждой строчки файла
    for line in input_file:
        # Добавляем "https://" в начале каждой строчки
        modified_line = 'https://' + line.strip()
        
        # записываем изменения в modified_line
        output_file.write(modified_line + '\n')

#print(f"URLs have been modified and saved to {output_file_path}.")

# Чтение URL адресов из файла
with open('modified_urls.txt', 'r', encoding='utf-8') as file:
    urls = [line.strip() for line in file]
    print("Read URLs from file:", urls)

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
