for feed_url in FEEDS: 
	feed = feedparser.parse(feed_url)
	if feed["bozo"] != 1:
		for item in feed["entries"]:
			url=item["links"][0]["href"]
			print "New URL detected: "+str(url)
			try:
				download(url.encode('unicode_escape'))
	except:
		print "Something failed"
	else:
		print "bad feed: " + feed_url
