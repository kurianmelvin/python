from mechanize import Browser
import re
import urllib
from bs4 import BeautifulSoup
regex = re.compile(r'<a[^>]*>([^<]+)</a>')
emails = []
pages = ['http://www.nasdaq.com/screening/companies-by-name.aspx?letter=']
visited = []




# # create a new instance of Browser class
# br = Browser()
# # Ignore robots.txt. Do not do this without thought and consideration.
# br.set_handle_robots(False)

# # fetch the stackoverflow.com url
# br.open("http://www.stackoverflow.com")

# # now we need to get the search form, so we get the first form
# # in page, which is the search form, in position 0
# br.select_form(nr=0)
# # now we set value of the search field with name property as 'q'.
# br.form['q'] = 'python'

# # submit the request
# response1 = br.submit()

# # print the response, by calling the read() method
# print response1.read()


while pages:
    url = pages.pop()
    print url
    visited.append(url)
    html = urllib.urlopen(url).read()
    for email in regex.findall(html):
        print email
        emails.append(email)        
    soup = BeautifulSoup(html)
    for link in soup.findAll('a'):
        href = link.get('href')
        if href and href.startswith('http://www.nasdaq.com/screening/companies-by-name.aspx?letter=&page=') and not href in visited:
            pages.append(href)
        
            
lines_seen = set()
with open('sto1.txt','w') as myfile:
    for item in emails:
        if item not in lines_seen:
            if 'Stock Quote' in item:
                myfile.write(item)
                lines_seen.add(item)
                stock= list(lines_seen)
                stock.sort()
            
myfile.close()
           
			
			
			
			




