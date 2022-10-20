import requests
from bs4 import BeautifulSoup
import pandas as pd

market_data = requests.get('https://www.marketwatch.com/market-data/cryptocurrency?mod=market-data-center')

# Create a BeautifulSoup object
soup = BeautifulSoup(market_data.text, 'html.parser')

# print pretty
print(soup.prettify())

#get the name of cryptocurrencies 
data = soup.find_all('td',class_='table_cell w55 ticker-negative')
data