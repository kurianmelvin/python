from mechanize import Browser
import re
import urllib
from bs4 import BeautifulSoup
regex = re.compile(r'<a[^>]*>([^<]+)</a>')
emails = []
pages = ['http://www.nasdaq.com/screening/companies-by-name.aspx?letter=']
visited = []

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
with open('stockAbbrv.txt','w+') as myfile:
    for item in emails:
        if item not in lines_seen:
            if 'Stock Quote' in item:
                myfile.write(item.split('Quote'))
                lines_seen.add(item)
                stock= list(lines_seen)
                stock.sort()
                
            
myfile.close()
           
			
			
			
			




