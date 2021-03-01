from bs4 import BeautifulSoup
import requests

#Requires #url, req, soup
#Extract titles from webpage

url="https://www.amazon.com/"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
print(soup.title)