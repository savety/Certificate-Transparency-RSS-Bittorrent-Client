#!/usr/bin/python
#
# Script to download .torrent files from a collection of rss feeds.
#   Copyright (C) 2009 Jamie Bennett
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   10-03-2009 First Version jamie@linuxuk.org

# List of url feeds to be parsed. This entry is just an _example_. Please
# do not download illegal torrents or torrents that you do not have permisson
# to own.
DOWNLOAD_DIR = "/home/jamie/downloads/torrents/"
TIMESTAMP    = "/home/jamie/downloads/rsstorrent.stamp"
VERBOSE      = True

import feedparser
import pickle
import os
import urllib2
from datetime import datetime 

items = []
feed_bad = False
current_file = " "

def download(url):
    """Copy the contents of a file from a given URL
    to a local file.
    """
    remote_file = urllib2.urlopen(url)
    
    # if this isn't a torrent file (probably from mininova) add a .torrent
    # extension
    if url[-7:] != "torrent":
        url += ".torrent"
        
    local_file = open('%s%s' % (DOWNLOAD_DIR, url.split('/')[-1]), 'w')
    local_file.write(remote_file.read())
    local_file.close()
    remote_file.close()

# Build up a list of torrents to check
for feed_url in FEEDS: 
    feed = feedparser.parse(feed_url)
    if feed["bozo"] != 1:
        for item in feed["entries"]:
            url=item["links"][0]["href"]
			print "New URL detected: "+str(url)
			try:
				download(url.encode('unicode_escape'))
    else:
		print "bad feed: " + feed_url
