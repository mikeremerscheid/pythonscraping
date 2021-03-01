import requests
from bs4 import BeautifulSoup

def scraper(acct):
    result = requests.get("https://www.twitter.com/" + acct)
    print(result.status_code)
    print(result.headers)
    print(result.url)
    src = result.content
    soup = BeautifulSoup(src,"lxml")
    posts = soup.find_all("article")
    print("\n")
    for post in posts:
        print(post.content)
        
        
scraper("berniesanders")