import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd

ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
print(header)
# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": "https://10.10.1.10:1080",
# }

data={'Title':[],'Price':[]}
# r=requests.get("https://api64.ipify.org?format=json")
# print(r.json())
# r=requests.get('https://api.ipify.org?format=json',proxies=proxies)
# print(r.json())


url="https://www.amazon.in/s?k=iphone&crid=1DMY9A2WXEYSA&sprefix=iphone%2Caps%2C232&ref=nb_sb_noss_2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r=requests.get(url,headers=header)


soup=BeautifulSoup(r.text,"html.parser")

# print(soup.prettify())

spans=soup.select("span.a-size-medium.a-color-base.a-text-normal")
# print(spans)
prices=soup.select("span.a-price")
for span in spans:
    data["Title"].append(span.string)

for price in prices:
    if not "a-text-price" in price.get("class"):
        data["Price"].append(price.find("span").get_text())

