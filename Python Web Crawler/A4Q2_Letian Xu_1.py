# Letian Xu
# 03-01-2019
# I have not given or received any unauthorized assistance on this assignment.

'''
Using the BeautifulSoup package to get the all pages belong to CDM websites;
Due to the deadline, I limitted the number of pages not excceded 500;
In the end, I using a for loop to get the content of all web address in my list, and convert the content to txt file.
Then, I will use another python file to count the word and its numebr.
'''

# import libraries
import operator
import requests
from bs4 import BeautifulSoup

text = []

def findtreasure():
    address = input('Tell me your homepage address: ')   
    findtreasure_help(address)

pages = set()

def findtreasure_help(address):
    soup = BeautifulSoup((requests.get(address)).text, "lxml")
    for link in soup.find_all('a'):
        try:
            if link.get('href').startswith('/') and '.aspx' in link.get('href'):
                myurl = address+link['href']
                if not myurl in pages:
                    pages.add(myurl)
                    if len(pages) >= 500:
                        break
                    else:
                        findtreasure_help(myurl)    
        except:
            pass

findtreasure()
print(len(pages))
pages = list(pages)

for item in pages:
    try:
        soup = BeautifulSoup((requests.get(item)).text, "lxml")
        text.append(soup.get_text())
    except:
        pass

f = open('CDM_500_pages.txt','w')
f.write(str(text))
f.close()