#!usr/bin/env/python

import urllib
import urllib.request
import urllib.error
import urllib.parse
import urllib.requests
import urllib.parse
import os
import sys

cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'


url="http://tinyurl.com/api-create.php?url="

if len(sys.argv) != 2:
    sys.exit(0);
if str(sys.argv[1]).find("http://") == -1 and  str(sys.argv[1]).find("https://") == -1:
	sys.argv[1]="http://"+sys.argv[1]
req=urllib.request.urlopen(url+str(sys.argv[1]))
data=req.read()
print("\033[0m\033[1m\033[36m~/link~ \033[0m\033[1m"+str(data))
