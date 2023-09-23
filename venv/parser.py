# подключаем urlopen из модуля urllib
from urllib.request import urlopen

# подключаем библиотеку BeautifulSout
from bs4 import BeautifulSoup

# очищаем код от выбранных элементов
def delete_div(code,tag,arg):
     # находим все указанные теги с параметрами
     for div in code.find_all(tag, arg): 
        # и удаляем их из кода
        div.decompose()

# очищаем текст по указанному адресу
def clear_text(url):
    # получаем исходный код страницы
    inner_html_code = str(urlopen(url).read(),'utf-8')
    # отправляем исходный код страницы на обработку в библиотеку
    inner_soup = BeautifulSoup(inner_html_code, "html.parser")
    # оставляем только блок с содержимым статьи
    inner_soup = inner_soup.find('div', {"class": 'article-content'})
    # удаляем титры
    #delete_div(inner_soup, "div", {'class':'wp-block-lazyblock-titry'})
    
    # удаляем боковые ссылки
    delete_div(inner_soup, "div", {'class':'wp-block-lazyblock-link-aside'})
   
    # удаляем баннеры
    for i in range(11):
        delete_div(inner_soup, "div", {'class':'wp-block-lazyblock-banner'+str(i)})
   
    # удаляем кат
    delete_div(inner_soup, "div", {'class':'accordion'})
    
    # удаляем преформатированный код
    delete_div(inner_soup, 'pre','')
  
    # удаляем вставки с кодом
    delete_div(inner_soup,'code','')
    
    # возвращаем содержимое страницы
    return(inner_soup.get_text())

print(clear_text('https://thecode.media/parsing/'))