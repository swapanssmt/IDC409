import requests
from bs4 import BeautifulSoup

url="https://www.findaphd.com/phds/?Keywords=data+science"
p=requests.get(url)
s=BeautifulSoup(p.content, "html.parser")
for a in s.find_all('a', href=True):
 print (a['href'])
