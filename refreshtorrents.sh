#!/bin/bash
#This script DOES NOT REFRESH TORRENTS. In fact, it only deletes the old .torrent files and redownload the available .torrents files and then import the newly downloaded files. Any new torrent will be added to transmission. Nothing will change for the old ones.
#QuickAndDirty
rm /tmp/torrents/*
python ~/Certificate-Transparency-RSS-Bittorrent-Client/rssfetcher.py
FILES=/tmp/torrents/*
for f in $FILES
do
  sudo transmission-remote -n 'transmission:transmission' -a $f
done
