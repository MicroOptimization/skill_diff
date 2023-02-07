from bs4 import BeautifulSoup
import re


#with open('cur_site/(10) flask developer Jobs in Canada _ LinkedIn.html', 'r') as f:
with open('cur_site/test.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, features="html.parser")

    mydivs = soup.find_all("h2", {"class": "target_class"}) #seems very useful
    print("---output:")
    print(mydivs)
    print(soup.find(string="small phrase"))
    print(soup.h1)

