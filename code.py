from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
headers = ["Name","Distance","Mass","Radius"]
star_data = []
temp_list = []
browser = requests.get(START_URL)

soup = BeautifulSoup(browser.text,"html.parser")

table = soup.find('table')

tr_tags = table.find_all('tr')
for i in tr_tags:
    td = i.find_all('td')
    row = [x.text.rstrip() for x in td]
    temp_list.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1,len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

data_frame = pd.DataFrame(list(zip(name,distance,mass,radius)),columns=['Star_name','Distance','Mass','Radius'])

data_frame.to_csv('stars.csv')