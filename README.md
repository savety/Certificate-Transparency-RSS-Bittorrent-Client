# Certificate-Transparency-RSS-Bittorrent-Client
A simple RSS client to fetch last Certificate Transparency Logs from [X-Cli project](https://github.com/X-Cli/ATBTCT).

## Requirements 
You need to have the transmission daemon running. You can install it by:
```sh
sudo apt-get install transmission-cli transmission-common transmission-daemon
```

## Default setup
By default, torrents will be downloaded to /tmp/torrents
This can be modified according to your transmission configuration in the setup.py

## Install and setup
```sh
mkdir /tmp/torrents
mkdir /incomplete-torrents
git clone https://github.com/savety/Certificate-Transparency-RSS-Bittorrent-Client.git
cd Certificate-Transparency-RSS-Bittorrent-Client
python rssfetcher.py
. asktorrent.sh
```

## Get New Torrents 
The simplest way to get new torrents and to process them is to run the script refreshtorrents.sh
```sh
. refreshtorrents.sh
```
You can also put the execution in a Crontab
```sh
30 2 * * *  . ~/Certificate-Transparency-RSS-Bittorrent-Client/refreshtorrents.sh
```
or to add it directly 
```sh
cd ~/Certificate-Transparency-RSS-Bittorrent-Client
crontab cron
```
