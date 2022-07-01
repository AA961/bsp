from turtle import ht
import requests
from bs4 import BeautifulSoup

url = "https://aa961.github.io"

r = requests.get(url)
htmlContent  = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

title = soup.div
# print(title)

divs = soup.find_all('button')
# print(divs)

classs = (soup.find('button')['class'])
# print(classs)

anyClass = soup.find_all("button",class_ = "btn")
# print(anyClass)

# fecthcing-text of tag
paraText = (soup.find('p').get_text())
# print(paraText)

#fetching whole text
wholeText = soup.get_text()
# print(wholeText)

#getting links
anchor = soup.find_all('a')
for link in anchor:
    # print(link.get('href'))
    pass
    
#rm repeated links
allLinks = set()
for link in anchor:
    if(link != "#"):
        link = "https://aa961.github.io" + link.get('href') 
        allLinks.add(link)
        
print(allLinks )