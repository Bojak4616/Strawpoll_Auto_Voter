#!/usr/bin/python

import requests
import threading
import sys
from random import randint

def worker(proxyDict, pollId, voteId):
	userAgents = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36", 
				"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"]

	headers = {'User-Agent' : userAgents[randint(0,2)]}
	try:
		#proxies=proxyDict,
		r = requests.get("http://strawpoll.me/" + str(pollId), headers=headers)
		cookies = {'__cfduid': r.cookies["__cfduid"]}
			
		vote = []
		vote.append(voteId)
		r = requests.post("http://strawpoll.me/api/v2/votes", headers=headers, cookies=cookies, proxies=proxyDict, json={"pollId":pollId, "votes": vote})
	except requests.exceptions.RequestException:
		global badProxies
		badProxies.append(proxyDict)
	
	print r.status_code


if __name__ == '__main__':
	badProxies = []

	with open('proxy.csv') as CSV:
		data = CSV.read()

	line = data.split('\n')
	numProxies = len(line)

	pollId = input("PollId: ")
	voteId = input("VoteId(Start at 0): ")

	for num in range(0,numProxies-1):
		proxy = line[num].split(',')
		
		if proxy[2] == 'yes':
			https = 'https'
		else:
			https = 'http'

		address = "http://" + proxy[0] + ':' + proxy[1]
		proxyDict = {https : address}


		t = threading.Thread(target=worker, args=(proxyDict, pollId, voteId, ))
		t.start()	

	while(True):
		if threading.activeCount() == 1:
			print "---------------------------------------------------------------"
			for bad in badProxies:
				print bad
			print "Done"
			sys.exit(0)