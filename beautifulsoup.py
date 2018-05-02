# parser: html BeautifulSoup(mk,'html.parser')
#         xml BeautifulSoup(mk,'xml')
#         html5lib BeautifulSoup(mk,'html5lib')

# BeautifulSoup Tag:tag
#               Name:name
#               Attributes:attrs
#               NavigableString:string
#               Comment
import requests
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")

# foreach:
# parents loop
# parent parent
# contents
# children
# descendants
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# next_sibling:next tag
# previous_sibling:previous tag
# next_siblings:iteration next
# previous_siblings:iteration previous
for sibling in soup.a.next_siblings:
    print(sibling)

print(soup.prettify())# print with dom format

# find_all(name,attrs,reclursive,string,**kwargs)
# name
print(soup.find_all(['a','b']))
# attrs
print(soup.find_all(id='link'))
# reclursive search all besides sons
print(soup.find_all('a',recursive=False))
# string
print(soup.find_all(string = 'Basic Python'))
# **kwargs
# find():one result
# find_parents():list
# find_parent():one result
# find_next_siblings():list
# find_next_sibling():one result
# find_previous_siblings():list
# find_previous_sibling():one result



