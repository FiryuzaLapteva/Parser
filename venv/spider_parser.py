import threading
import requests
from bs4 import BeautifulSoup
import json
import csv

def url_mod(input_file_path, output_file_path):

# открываем исходный файл для чтения и изменный файл для записи
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Итеративно проходим по каждой строчки файла
        for line in input_file:
        # Добавляем "https://" в начале каждой строчки
            modified_line = 'https://' + line.strip()

        # записываем изменения в modified_line
            output_file.write(modified_line + '\n')

#print(f"URLs have been modified and saved to {output_file_path}.")

<<<<<<< HEAD
url_mod('ru.txt', 'modified_urls.txt')

=======
url_mod('urls.txt', 'modified_urls.txt')
>>>>>>> 2a78b2ea1f65316b86af7b30de8ffa27a6087667
# Чтение URL адресов из файла
with open('modified_urls.txt', 'r', encoding='utf-8') as file:
    urls = [line.strip() for line in file]
#    print("Read URLs from file:", urls)

class Parser(threading.Thread):
   # Класс парсера

    def __init__(self, url, lock):
        threading.Thread.__init__(self)
<<<<<<< HEAD
        self.url = url[:1000]
=======
        self.url = url
>>>>>>> 2a78b2ea1f65316b86af7b30de8ffa27a6087667
        self.lock = lock

    def run(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                soup = soup.find_all('h1')
                print(f'Запрос выполнен успешно для URL: {self.url}')
                spider_file = 'parsed_data.csv'
                with open(spider_file, mode='a', newline='', encoding='utf-8') as file:
                    csv_writer = csv.writer(file)
                    # Пройтись по распарсенным данным и записать каждую строку
                    for h1 in soup:
                        row = [self.url, h1.text]  # Определить данные для каждой строки
                        csv_writer.writerow(row)
            else:
                print(f'Произошла ошибка при выполнении запроса для URL: {self.url}')
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при запросе для URL: {self.url}, {e}')

# Создайте строку заголовка для CSV-файла (если необходимо)
header = ['url', 'content']

# Откройте CSV-файл в режиме записи и запишите заголовок
with open('parsed_data.csv', mode='w', newline='', encoding='utf-8') as file:
<<<<<<< HEAD
    csv_writer = csv.writer(file, quotechar='', quoting=csv.QUOTE_NONE)
=======
    csv_writer = csv.writer(file)
>>>>>>> 2a78b2ea1f65316b86af7b30de8ffa27a6087667
    csv_writer.writerow(header)
          
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
