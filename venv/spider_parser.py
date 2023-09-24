import threading
import requests
from bs4 import BeautifulSoup
import json

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

url_mod('urls.txt', 'modified_urls.txt')
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
        scraped_data = []
        #Запуск обработки
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                soup = soup.find_all('h1')
                print(f'Запрос выполнен успешно для URL: {self.url}')
                for h1 in soup:
                    scraped_data.append({'url': url, 'content': h1.text})
                    #Добавим спарсенные данные в spider_file.json
                    with open('spider_file.json', 'a', encoding='utf-8') as file:
                        json.dump(scraped_data, file, ensure_ascii=False, indent=4)
            else:
                print(f'Произошла ошибка при выполнении запроса для URL: {self.url}')
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при запросе для URL: {self.url}, {e}')
            
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
