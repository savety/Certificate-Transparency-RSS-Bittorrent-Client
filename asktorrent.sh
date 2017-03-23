#!/bin/bash
FILES=/tmp/torrents/*
for f in $FILES
do
  transmission-remote -n 'transmission:transmission' -a $f
done
