
import requests
from bs4 import BeautifulSoup
import re

url = input("Enter URL:")
name = input("Website Name:")

# file = open(url + ".txt", "x")
# file = open(url+'.txt', 'w')


def gettingData(url):
    file = open(name + " " + "pagedata.txt", "x")
    
    
    file.write("\n -----------------pageData----------------- \n")

    r = requests.get(url)
    htmlContect = r.content

    soup = BeautifulSoup(htmlContect, 'html.parser')

    textData = (soup.prettify())
    strData = soup.get_text().strip()
    pattern = re.compile("[\n]{3,}")
    finalData = re.sub(pattern,"",strData)
    file.write(finalData)

    return textData
    # print(textData)


def gettingLinks(textData,url):
    file = open(name + " " + "links.txt", "x")
    
    

    soup = BeautifulSoup(textData,'html.parser')
    anchor = soup.find_all('a')
    
    allLinks = set()
    
    for link in anchor:
        if link != "#":
            link = url + link.get('href')
            allLinks.add(link)
    file.write("\n --------------------links----------------------- \n")
    strLinks = str(allLinks)
    pattern = re.compile("[\n]{4,}")
    finalData = re.sub(pattern,"",strLinks)
    file.write(finalData)
            
    return allLinks

    


def linkData(allLinks):
    file = open(name + " " + "allpages.txt", "x")
    

    for url in allLinks:
        # file = open(name + "all.txt", "w")
        
        file.write("\n \n -----------------links data --------------- \n \n" + url + "\n \n \n")
        r = requests.get(url)
        htmlLinksData = r.content
        soup = BeautifulSoup(htmlLinksData, 'html.parser')
        linkData = (soup.prettify())
        fullData = soup.get_text().strip()
        
        pattern = re.compile("[\n]{3,}")
        finalData = re.sub(pattern,"",fullData)
        file.write(finalData)
        
        
        
       
 


Data = gettingData(url)
allLinks = gettingLinks(Data,url)
allData = linkData(allLinks)
