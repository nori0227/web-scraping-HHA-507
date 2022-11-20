import requests
from bs4 import BeautifulSoup
import pandas as pd

market_data = requests.get('https://www.marketwatch.com/market-data/cryptocurrency?mod=market-data-center')

# Create a BeautifulSoup object
soup = BeautifulSoup(market_data.text, 'html.parser')

# print pretty
print(soup.prettify())

#get the cryptocurrencies row
data = soup.find_all('tr', class_='table__row')
data
output_data = []
for i in data:  #for x in y: 
    print(i.text) 
    data = i.text
    output_data.append(i.text)

len(output_data)
list(output_data)
output_data[1]
output_data[3]
output_data[5]

# get the name of the ticker-negative cryptocurrencies only
ticker_positive= soup.find_all('td', class_='table__cell w55 ticker-positive')
ticker_positive
output_ticker_positive = []
for i in ticker_positive: 
    print(i.text)
    ticker_positive = i.text
    output_ticker_positive.append(i.text)

len(output_ticker_positive)
list(output_ticker_positive)
output_ticker_positive[1]
output_ticker_positive[3]

#get the last value for positive-ticker cryptocurrencies
last_value = soup.find_all('td', class_='table__cell w15')
last_value

output_last_value = []
for i in last_value:
    print(i.text)
    last_value = i.text
    output_last_value.append(i.text)

len(output_last_value)
list(output_last_value)
output_last_value[2]


list1= output_data
list2= output_ticker_positive
list3 = output_last_value
#create dictionary
dictionary = {'ticker_positive': list2}

## put this together in a dataframe
df = pd.DataFrame({'ticker_positive':output_ticker_positive})
df.to_csv('/Users/nuri/web-scraping-HHA-507/Data/cryptocurrencies.csv')

