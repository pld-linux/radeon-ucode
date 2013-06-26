#!/bin/sh
# TODO:
# - make it really update spec file

url="http://people.freedesktop.org/~agd5f/radeon_ucode/"

i=1
for a in $(lftp -c "open $url; cls -1 *.bin"); do
	echo "Source${i}:	$url$a"
	echo "# Source${i}-md5:	x"
	i=$((i+1))
done

j=1
while [ $j -lt $i ]; do
	echo "		%{SOURCE${j}} \\"
	j=$((j+1))
done
