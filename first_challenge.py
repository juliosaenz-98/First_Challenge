
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from datetime import datetime, timedelta, date

data=dict()
scraped_df = pd.DataFrame() 
  # Mention the URL of website here from which you want to scrape
url = 'https://www.poynter.org/?ifcn_misinformation=the-colombian-city-of-manizales-had-its-highest-development-peaks-after-world-wars'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.content, 'html.parser')
page_elements = soup.find_all('div', attrs={'class': 'post-container'})
for ele in page_elements:
  temp = []
  ele_str= str(ele.text)
  else_str_split = ele_str.splitlines()

  fact_check_temp = else_str_split[2]
  fact_check = fact_check_temp
  data['Fact_checked_by'] = re.split('[-:]', fact_check_temp)[2]
  date_country = else_str_split[3]
  data['Date']  = re.split('[-|]', date_country)[0]
  data['Country']  = re.split('[-|]', date_country)[1]
  label_text = else_str_split[5]
  data['Text'] = re.split('[-:]', label_text)[1]
  data['Label'] = re.split('[-:]', label_text)[0]
  text_explanation  = else_str_split[10]
  data['Explanation'] = re.split ('[-:]', text_explanation)[1]
  text_origin = else_str_split[13]
  data['Origin'] = re.split ('[-:]', text_origin)[1]

  temp.append(data)
  scraped_df = scraped_df.append(temp)
scraped_df.to_csv('First_Challenge_scraped_data.csv')
print("Scrapping Completed")
