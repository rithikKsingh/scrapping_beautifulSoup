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
print(soup.prettify())
