import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os
from PIL import Image

with open("data/Constituencies.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())
table = soup.find_all("table")[0]
thead = table.find('thead')
thead_titles = thead.find_all('th')
thead_table_titles = [title.text.strip() for title in thead_titles]

# Extracting headers from <tfoot>
tfoot = table.find('tfoot')
tfoot_titles = tfoot.find_all('th')
tfoot_table_titles = [title.text.strip() for title in tfoot_titles]

tbody = table.find('tbody')
rows = tbody.find_all('tr')

data = []
for row in rows:
    cells = row.find_all('td')
    cell_data = [cell.text.strip() for cell in cells]
    data.append(dict(zip(thead_titles, cell_data)))
df = pd.DataFrame(data, columns=thead_titles)





# Creating the DataFrame
#df = pd.DataFrame(data, columns=thead_titles)
#print(df)
#print("Thead Titles:", thead_table_titles)
#print("Tfoot Titles:", tfoot_table_titles)

#output_file = 'table_data.json'
#df.to_json(output_file, orient='records', lines=True)
df.to_csv(r'E:\KALVIUM\data\ParliamentaryConstituencies.csv', index = False)
#print(f"Data saved to {output_file}")