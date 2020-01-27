#!/usr/bin/env python3
#
#
"""rest_helper.py

Usage:
    rest_helper.py [-v] [-n=<count>|--num=<count>] [-c=<fname>|--config=<fname>]
    rest_helper.py (-h | --help)
    rest_helper.py (-V | --version)

Options:
    -h --help                 Show this screen and exit
    -V --version              Show Version and exit
    -v                        be a lot more verbose
    -n count --num=count      number of parallel threads [default: 1]
    -c fname --config=fname   config filename [default: config.ini]

"""
from docopt import docopt
import sys
import re
import threading


verbose = False
thread_count = 1
conf_fname = 'config.ini'

class Service:
    """ class Service, containing all necessary datas
    strings: username, url, urlpath """
    def __init__(self, username, urlpath, url):
        self.username = username
        self.urlpath = urlpath
        self.url = url
    def http_auth(self):
        o_url = re.split('://', self.url)
        if verbose:
            print(o_url)
        return o_url[0] + '://' + self.username + '@' + o_url[1]

#    username = 'testuser'
#    urlpath = '/rest/1.0/request'




#-----------------------------------------------------------------
# functions, etc.
#-----------------------------------------------------------------

def read_configfile(configfilename='config.ini'):
    """ function, reading key-value pairs from ini-file (MS-style)
    the argument is the filename with defaulting 'config_name'
    The return value is an exit code to be passed to sys.exit(); it
    may be None to indicate success."""

#    import ConfigParser
    import configparser
    work_url = []

    c = configparser.ConfigParser()
    c.read(configfilename)
    sec = c.sections()
    if verbose:
        print(sec)

    try:
        user = c['Data']['username']
        path = c['Data']['urlpath']

        for i in range(1,5):
            help_str = 'url'+str(i)
            work_url.append(Service(user, path, c['Urls'][help_str]))
            if verbose:
                print(work_url)
    except:
        print("""Error: could not read config file options from %s .\n""" % configfilename)
        return 3

    return work_url


def worker_thread(service_url):
    """ worker function, just print the service_url
    return value is none """
    print(service_url.http_auth())



#-----------------------------------------------------------------
# start of main part of programm
#-----------------------------------------------------------------

if __name__ == '__main__':
    arguments = docopt(__doc__, version="Version: 0.91")
#    print(arguments)

verbose = arguments['-v']
conf_fname = arguments['--config']
thread_count = int(arguments['--num'])
if thread_count > 4:
    print("Warning, a maximum of 4 parallel threads allowed.")
    print("         number of threads is set to 4. (thread_count=4)\n")
    thread_count = 4
elif thread_count < 1:
    print("Warning, a minimum of 1 thread is necessary.")
    print("         number of threads is set to 1. (thread_count=1)\n")
    thread_count = 1

if verbose:
    print("cmd_line arguments: ", arguments)
    print("      thread_count: ", thread_count)
    print("   config filename: ", conf_fname)

urls = read_configfile(conf_fname)
if not isinstance(urls, list):
    print("Error in func read_configfile, wrong return type, should be type list\n")
    sys.exit(4)
    
if verbose:
    print(urls)
    
threads = []
for i in range(thread_count):
    if verbose:
        print("number : ", i, "\t url: ", urls[i].url)
    t = threading.Thread(target = worker_thread, args=(urls[i],))
    threads.append(t)
    t.start()

if verbose:
    print("finished python exercise\n")




