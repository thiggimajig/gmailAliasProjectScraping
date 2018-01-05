#make array of all members pages
#do the url go to thing
#scrape out the names F0XO1GC-Ob-d g-hovercard with span class find all beautiful soup
#or span class _username
#write to a csv the URL and the names 
#or span class name of alias F0XO1GC-ab-f F0XO1GC-b-Yb 
#
#maybe this for t in tickers:
#     html = requests.get(t).text
#     soup = BeautifulSoup(html, "html.parser")
#     officer_table = soup.find('table', {"class" : "dataTable"})

#     https://stackoverflow.com/questions/40903412/beautiful-soup-looping-through-array-of-urls
#     
#or maybe use this?    https://stackoverflow.com/questions/35732464/looping-through-a-list-of-urls-for-web-scraping-with-beautifulsoup
#
#or this to figure out how to find all with beautiful soup https://stackoverflow.com/questions/16322862/beautiful-soup-findall-doent-find-them-all
#
import requests
import csv
from lxml import html
import re
import requests
from bs4 import BeautifulSoup

quote_page = open('Analytics Support - Google Groups.html')
line = quote_page.readline()
quote_page.close()


print(quote_page)
#page = requests.get(quote_page)
#text = page.content
soup = BeautifulSoup(line, 'html.parser')
print(soup)

f = csv.writer(open("analyticsSupport.csv", "w"))
f.writerow(["Names"])

for element in soup.findAll('div', {'class':'F0XO1GC-Ob-c'}):
	memberNames = element.get_text()
	print(memberNames)
	f.writerow([memberNames])


#saying memberNames is undefined? weird 
#now it's not, but it's not scraping anything
#maybe because of password? can we try saving each page to my
#harddrive then scraping that? doesn't violate googles TOS either
#maybe do in macros then? 
#save as then scrape out 