import sys
import re
import socket
import requests
import untangle
import humanize
import colorama
from colorama import Fore, Back, Style

def noarguments():
    print('Usage: python script.py sitelist.txt')
    sys.exit(0)

if len(sys.argv) != 2:
    noarguments()

sitelist = sys.argv[1]
subdomainurl2 = ".s3.amazonaws.com"

def s3parse(url):
    xml = untangle.parse(url)
    try: xml.ListBucketResult.Contents[0].Key.cdata is None
    except IndexError: print xml.ListBucketResult.Name.cdata + " --> Could not see any content" #some S3 buckets do not show files
    else:
        print Fore.GREEN + xml.ListBucketResult.Name.cdata #print S3 Bucket name
        x = 0
        while x < len(xml.ListBucketResult.Contents):
            print Fore.YELLOW + xml.ListBucketResult.Contents[x].Key.cdata + " - " + humanize.naturalsize(xml.ListBucketResult.Contents[x].Size.cdata) #print filename and filesize
            x += 1
            print(Style.RESET_ALL) #trust me you want to keep this line


def subdomain():
    url = 'http://' + line.rstrip() + subdomainurl2
    r = requests.get(url)
    if r.status_code != 403 and r.status_code != 404:
        s3parse(url)


with open(sitelist) as f:
    for line in f:
        subdomain()
