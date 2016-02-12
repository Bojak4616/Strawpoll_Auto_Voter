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

Add the poll id on lines in strawpoll.py:

https://github.com/Bojak4616/Strawpoll_Auto_Votes/blob/master/strawpoll.py#L16

https://github.com/Bojak4616/Strawpoll_Auto_Votes/blob/master/strawpoll.py#L21


Change the '2' to the vote you want to be pushed. Strawpoll indexs votes starting at 0:

https://github.com/Bojak4616/Strawpoll_Auto_Votes/blob/master/strawpoll.py#L20
<br></br>
<strong>Step 3</strong>

Run strawpoll.py
<br></br>
<strong>Step 4</strong>

Profit
