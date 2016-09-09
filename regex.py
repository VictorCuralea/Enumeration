import sys
import re

#this file lets you parse top-1m.csv

readfile = sys.argv[1]
with open(readfile) as f:
    for line in f:
	try:
	    p = re.compile('(.*),(.*)(\.)')
	    match = re.match(p,line)
	    print match.group(2)
	except Exception:
	    pass

exit()
