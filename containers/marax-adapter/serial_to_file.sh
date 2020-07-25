while read LINE; do
  echo "$LINE" >> $1;
done < $2
