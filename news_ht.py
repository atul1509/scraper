from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

#  probably because of mod_security or some similar server security feature setting a known browser user agent
ht = Request("https://www.hindustantimes.com/", headers={'User-Agent': 'Mozilla/5.0'})

page = urlopen(ht).read()

soup = BeautifulSoup(page, "lxml")

all_links = soup.find_all("a")
head_lines=[[]]
for link in all_links:
	
	link = str(link)
	if ("https://www.hindustantimes.com" in link):
		part = link.split(">")
		
		if (len(part[-2]) > 30):	#
			part[-2] = str(part[-2])
			head = part[-2].split("<")
			
			head_lines.append(head[0])

print(head_lines[-1])   # to check
with open("ht_headlines", "w") as f:
	writer = csv.writer(f)
	n = 1
	for headline in head_lines:
		headline = str(headline)
		num = str(n)+". "
		f.write(num)
		f.write(headline)
		f.write("\n")
		n+=1

