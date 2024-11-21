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

# print(soup.select("div.italic")) #gives a list of all the divs with class italic

# print(soup.select("span#italic")) #gives a list of all the spans with class italic
    
# print(soup.div.get("class")) # returns the list of class names of the first div. If first div doesn't contain any classes, it shows none

# print(soup.span.get("id")) #returns the id of first span

# print(soup.find(class_="italic"))  #class is a reserved keyword, so use class_. it returns the first tag with class attribute
# print(soup.find_all(class_="italic")) # returns a list of all the tags with class attribute
# print(soup.find(id="firstSpan"))  #returns first tag with id 

# for child in soup.find(class_="container").children:
#     print(child)
#prints all the childs of the particular elements

# for parent in soup.find(class_="box").parents:
#     print(parent)
#prints all the parents of the element


# here it only modifies the output
# cont=soup.find(class_="container")
# cont.name="span"
# cont["class"]="myClass class2"
# cont.string="I am a string"
# print(cont)



# adding a htnl tag
# ulTag=soup.new_tag("ul")

# liTag=soup.new_tag("li")
# liTag.string="First point"
# ulTag.append(liTag)

# liTag=soup.new_tag("li")
# liTag.string="Sec point"
# ulTag.append(liTag)

# soup.html.body.insert(0,ulTag) #here we are adding tag to the soup object containing html, not the html file itself
# with open("modified.html","w") as f:
#     f.write(str(soup))  #here we need to convert the soup object into a string otherwise it will show error



# returns true or false based on whether the tag has that attribute or not 
# cont = soup.find(class_="container")
# print(cont.has_attr("contenteditable"))


# prints all the elements which as attribute class but not id
# def has_class_but_not_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")

# results=soup.find_all(has_class_but_not_id)
# print(results)