import sys
import re
import socket
import colorama
from colorama import Fore, Back, Style


def noarguments():
    print('Usage: python script.py website.com subdomainlist.txt')
    sys.exit(0)

if len(sys.argv) != 3:
    noarguments()


site = sys.argv[1] #the website you want to enumerate
dnslist = sys.argv[2] #list of subdomains


def bruteforce():
    with open(dnslist) as f:
        for line in f:
            subdomain = line.rstrip() + "." + site
            targetIP = socket.gethostbyname(subdomain)
            if targetIP is None:
                print Fore.GREEN + socket.gethostbyname(subdomain) + " - " + subdomain
                print(Style.RESET_ALL)
                for i in range(1,10000):
                    s = socket(AF_INET, SOCK_STREAM)
                    s.settimeout(1)
                    result = s.connect_ex((targetIP, i))
                    if(result == 0):
                        print 'Port %d: OPEN' % (i,)
                    s.close()


bruteforce()
