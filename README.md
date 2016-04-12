# Strawpoll_Auto_Votes
<strong>Disclaimer: Using random proxies will result in malicious traffic coming to your box. Use at your own risk</strong>

This is not optimized to be user friendly. Those changes will be added when I have time...
<br></br>
<strong>Step 1</strong>

Run proxy-list.py to gather 300 proxies. 1 proxy = 1 vote, many will not work.

The website refreshes every 10min so throw it in a cron job to populate overnight.

Script checks for duplicate entries.
<br></br>
<strong>Step 2</strong>

Gather the poll ID (ex http://strawpoll.me/<strong>6598212</strong>)

Run strawpoll.py and you will be prompted for the pollId and then the vote you wish to cast

*Note* Strawpoll's vote options start at 0
<br></br>

<strong>Step 3</strong>

Profit

<br></br>
TODO: 

Clean up proxy-list.py and have it precheck if a proxy will return a 200 status code

Add selecting multiple options on one vote, if enabled by poll creator.