# import requests


# def fetchAndSaveToFile(url,path):
#     r=requests.get(url)
#     with open(path,"w") as f:
#         f.write(r.text)

# url="https://timesofindia.indiatimes.com/city/delhi"

# fetchAndSaveToFile(url,"data/times.html")
from bs4 import BeautifulSoup

with open ("sample.html",'r') as f:
    html_doc=f.read()

soup=BeautifulSoup(html_doc,"html.parser")
# print(soup.prettify())

# print(soup.title) #output: <title>Rithik_Title</title>

# print(soup.title.string) #output: Rithik_Title

# print(soup.div) #gives first div

# print(soup.find_all("div")) #gives all divs
# print(soup.find_all("div")[1]) #gives first div

# for link in soup.find_all("a"):
#     print(link.get("href"))
# prints all the links in href attribute

# s=soup.find(id="link3")
# print(s.get("href"))
#  to get particular id

# for link in soup.find_all("a"):
#     print(link.get_text())
# prints the text inside the tags. work same as link.string