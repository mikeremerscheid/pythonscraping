from bs4 import BeautifulSoup
import requests
#url, req, soup
url="https://finance.yahoo.com/"
req=requests.get(url)
soup=BeautifulSoup(req.text, "html.parser")
for link in soup.find_all('img'): #tag name
    print(link.get('src')) #class name
    
    
    