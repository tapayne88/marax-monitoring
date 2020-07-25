#!/bin/sh

while read LINE; do
  if [ "$LINE" != "" ]; then
    echo "$(date +%s),$LINE" >> $2;
  fi
done < $1
