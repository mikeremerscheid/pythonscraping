import bs4 as bs
import urllib.request

url = 'https://www.twitter.com/'
sauce=urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, 'lxml')

print(soup.title.text)
