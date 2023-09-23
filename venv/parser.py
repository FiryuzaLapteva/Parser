# подключаем urlopen из модуля urllib
from urllib.request import urlopen

# подключаем библиотеку BeautifulSoup
from bs4 import BeautifulSoup

# получаем исходный код страницы
inner_html_code = str(urlopen('https://mipt.ru/?ysclid=lmvthwtyqo439744876').read(),'utf-8')

# отправляем исходный код страницы на обработку в библиотеку
inner_soup = BeautifulSoup(inner_html_code, "html.parser")

# выводим содержимое страницы
print(inner_soup.get_text())