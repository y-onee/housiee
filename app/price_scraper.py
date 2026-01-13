import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.viewpoint.ca/show/property/15463391/1/7584-Main-Street-Louisbourg-206'

def fetch_price_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    element = soup.find_all('div', class_='span4 box')
    list = element[0].find_all('li')
        
    for element in list:
        values = element.find_all('span', class_='span5')
        pre_string =values[0].get_text()
        post_string = re.sub(r'[^0-9.]', '', pre_string)
        print(post_string)
    
        
fetch_price_data(url)