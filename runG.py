#!forumsearch/

import urllib.request #urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime

soup = BeautifulSoup(open("allGG.html"), "lxml")

f = csv.writer(open("aliases.csv", "w"))
f.writerow(["Alias Group Name", "Google Group Alias URL"])

links = soup.find_all('a', attrs={'class':'gwt-Anchor F0XO1GC-c-a'})

for link in links:
	names = link.contents[0]
	fullLink = link.get('href')
	print(names)
	print(fullLink)
	#if 'class' == 'gwt-Anchor F0XO1GC-c-a': #didn't work 
	#print(link)
	
	f.writerow([names, fullLink]) 

#prints it all in a pretty html format 
#print(soup.prettify())


'''allAliasesArray = []

for a in soup.findAll('a', attrs={'class':'gwt-Anchor F0XO1GC-c-a'}):
	allAliasesArray.append(a.text)
	#print(table.text)
	#print(allAliasesArray)

#groups =  soup.find_all('a', attrs={'class':'gwt-Anchor F0XO1GC-c-a'})

with open('indexB.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([allAliasesArray, datetime.now()])'''

