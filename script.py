import requests
from bs4 import BeautifulSoup

f = open('data.txt','x')
file = open("data.txt",'w')


def gettingData(url):

    r = requests.get(url)
    htmlContect = r.content

    soup = BeautifulSoup(htmlContect, 'html.parser')

    textData = (soup.prettify())
    strData = soup.get_text().strip()
    # textData.strip()
    file.write(strData)

    return textData
    # print(textData)


def gettingLinks(textData,url):

    soup = BeautifulSoup(textData,'html.parser')
    anchor = soup.find_all('a')
    allLinks = set()
    
    for link in anchor:
        if link != "#":
            link = url + link.get('href')
            allLinks.add(link)
            strLinks = str(allLinks)
            file.write(strLinks)
            
            return allLinks

    


def linkData(allLinks):
    for url in allLinks:
        r = requests.get(url)
        htmlLinksData = r.content
        soup = BeautifulSoup(htmlLinksData, 'html.parser')
        linkData = soup.get_text()
        file.write(linkData)
        file.close()
        return linkData


url = input("Enter URL:")
Data = gettingData(url)
allLinks = gettingLinks(Data,url)
allData = linkData(allLinks)
# print(allData)