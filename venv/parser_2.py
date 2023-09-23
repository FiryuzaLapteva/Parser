
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

url = "https://zanauku.mipt.ru//"
inner_html_code = str(urlopen(url).read(), 'utf-8')
inner_soup = BeautifulSoup(inner_html_code, "html.parser")
inner_soup = inner_soup.find_all('h2', class_='entry-title grid-title')

# Create a list to store the article titles
article_titles = [inner.text for inner in inner_soup]

# Save the list of article titles to a JSON file
with open('file.json', 'w', encoding='utf-8') as file:
    json.dump(article_titles, file, ensure_ascii=False, indent=4)

print("Article titles have been saved to file.json")
