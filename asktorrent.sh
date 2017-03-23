#!/bin/bash
FILES=/tmp/torrents/*
for f in $FILES
do
  transmission-remote -n 'transmission:transmission' -a $f #NB: transmission:transmission is the default credentials
done
