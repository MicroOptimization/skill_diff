from bs4 import BeautifulSoup
import re
soup1 = BeautifulSoup("<p>Some<b>bad at 12 everything<i>HTML", features="html.parser")

soup = BeautifulSoup("See how you compare to 283 applicants", features="html.parser")

search_phrase = "See how you compare"
applicant_string = str(soup(string=re.compile(search_phrase)))
num_applicants = re.findall('\d+', applicant_string)
print(num_applicants)

#print(soup.prettify())
"""
print("--")
print(soup.find(string="bad"))
print(soup.findAll(string="bad at everything"))
print(soup.i)
"""

#with open('cur_site/(10) flask developer Jobs in Canada _ LinkedIn.html', 'r') as f:
with open('cur_site/test.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, features="html.parser")

    mydivs = soup.find_all("h2", {"class": "target_class"}) #seems very useful
    print("---output:")
    print(mydivs)
    print(soup.find(string="small phrase"))
    print(soup.h1)

