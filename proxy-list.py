#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

if __name__=="__main__":
	r = requests.get("http://free-proxy-list.net/")
	
	ip = []
	port = []
	https = []
	count = 0
	soup = BeautifulSoup(r.content, 'html.parser')
	for coulmn in soup.find_all('td'):
		count +=1
		if count == 1:
			ip.append(coulmn.text)

		if count == 2:
			port.append(coulmn.text)

		if count == 7:
			https.append(coulmn.text)
		
		if count == 8:
			count = 0

	#Wow this could use some fixing
	with open("proxy.csv", 'w') as CSV:
		pass

	with open("proxy.csv", 'r') as CSV:
		allText = CSV.read()
	
	with open("proxy.csv", 'a') as CSV:
		for num in range(0, len(ip)):
			if allText.find(ip[num]) != -1:
				continue

			CSV.write(ip[num] + ',' + str(port[num]) + ',' + https[num] + '\n')