from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

# Create an empty list to store all article titles
all_article_titles = []

# Define the base URL and the number of pages to scrape
base_url = "https://zanauku.mipt.ru//page/"
num_pages = 5  # Change this to the number of pages you want to scrape

for page_number in range(1, num_pages + 1):
    # Construct the URL for the current page
    url = f"{base_url}{page_number}/"
    
    inner_html_code = str(urlopen(url).read(), 'utf-8')
    inner_soup = BeautifulSoup(inner_html_code, "html.parser")
    inner_soup = inner_soup.find_all('h2', class_='entry-title grid-title')
    
    # Extract and append the article titles to the list
    article_titles = [inner.text for inner in inner_soup]
    all_article_titles.extend(article_titles)

# Save all the article titles to a JSON file
with open('file_parser_2.json', 'w', encoding='utf-8') as file:
    json.dump(all_article_titles, file, ensure_ascii=False, indent=4)

print(f"Scraped {len(all_article_titles)} article titles from {num_pages} pages.")
