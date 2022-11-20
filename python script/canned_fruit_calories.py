import requests
from bs4 import BeautifulSoup
import pandas as pd

cannedfruit_cal = requests.get ('https://www.calories.info/food/canned-fruit')
cannedfruit_cal

# Create a BeautifulSoup object
soup = BeautifulSoup(cannedfruit_cal.text, 'html.parser')

# print pretty
print(soup.prettify())

## 1. get the name of canned food
foodname = soup.find_all('td', class_='food') ## look at the dropdown
foodname

output_foodname = []
for i in foodname:
    print(i.text)
    foodnames = i.text
    output_foodname.append(i.text)

len(output_foodname)
list(output_foodname)
output_foodname[1]
output_foodname[3]
output_foodname[5]

list1 = output_foodname

### 2. get the calories
serving_portion = soup.find_all('td', class_='serving portion')
serving_portion

output_serving_portion = []
for i in serving_portion:
    print(i.text)
    serving_portion = i.text
    output_serving_portion.append(i.text)

len(output_serving_portion)
list(output_serving_portion)
output_serving_portion[6]

list2 = output_serving_portion

## 3. get the calories
kcal_portion = soup.find_all('td', class_= 'kcal')
kcal_portion

new = soup.find_all('td')

output_kcal_portion = []
for i in kcal_portion:
    print(i.text)
    kcal_portion = i.text
    output_kcal_portion.append(i.text)

len(output_kcal_portion)
list(output_kcal_portion)
output_kcal_portion[6]

list3 = output_kcal_portion

##create dictionary
dictionary = {'foodname': list1, 'serving_portion': list2, 'kcal_portion': list3}

df = pd.DataFrame({'foodname':output_foodname, 'serving_portion':output_serving_portion, 'kcal_portion': output_kcal_portion})

df.to_csv('/Users/nuri/web-scraping-HHA-507/Data/cannedfruits_calories.csv')



