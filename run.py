from ntpath import join
import requests
import pandas
from bs4 import BeautifulSoup
import sys

#choose website to scrape with CL argument
#url = sys.argv[1]

#choose website to scrape with code
url = "https://en.wikipedia.org/wiki/List_of_mass_shootings_in_the_United_States#1920s"

#scrape data from website
soup = BeautifulSoup(requests.get(url).content, 'html.parser')

#delete all superscripted characters from data
for sup in soup.select('sup'):
    sup.extract()

#delete all subscripted characters from data
for sub in soup.select('sub'):
    sub.extract()

#feed data into pandas
tables_on_page = pandas.read_html(str(soup))

#create dataframe and populate with first table on page
df = tables_on_page[0]

#loop through next 13 tables and add them to the dataframe
for i in range(1,14): 
    data = tables_on_page[i]
    df = pandas.concat([df, data], join="inner")
    i = i + 1

#loop through 2 irrelevant tables and do nothing
for i in range(14, 16):
    i = i+  1

#loop through remaining 8 tables and add them to the dataframe
for i in range(16,24):
    data = tables_on_page[i]
    df = pandas.concat([df, data], join="inner")
    i = i + 1


df.to_json("table.json", index=False, orient='table')