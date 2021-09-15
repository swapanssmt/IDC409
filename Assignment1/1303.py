import requests                           # importing request package allows to send HTTP requests using Python.
from bs4 import BeautifulSoup             # importing bs4 from BeautifulSoup package
file1 = open("Output.txt","a")            # to create a file named "output.txt"
file1.write("...........................Page1........................\n")  # write to a file
file1.write("\n")     # write to a file
file1.write("\n")     # write to a file
url="https://www.findaphd.com/phds/?Keywords=data+science"   # variable to store string
p=requests.get(url)                       # The GET sends the encoded user information appended to the page request and used to retrieve information from the given server
s=BeautifulSoup(p.content, "html.parser")
for a in s.find_all('a', href=True):
    file1.write(a['href'])
    file1.write("\n")
file1.write("\n")
file1.write("\n")
for i in range(2,42):
    file1.write("...........................Page")
    file1.write(str(i))
    file1.write("........................\n")
    file1.write("\n")
    file1.write("\n")
    link="https://www.findaphd.com/phds/?Keywords=data+science&PG="
    flink=link+str(i)
    p=requests.get(flink)                       # The GET sends the encoded user information appended to the page request and used to retrieve information from the given server
    s=BeautifulSoup(p.content, "html.parser")
    for a in s.find_all('a', href=True):
        file1.write(a['href'])
        file1.write("\n")
