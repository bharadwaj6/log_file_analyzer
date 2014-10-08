"""
    Author: Bharadwaj Srigiriraju

    A simple log file analyzer.

"""

import re

ip_adresses = {}
page_titles = {}
urls = {}
ids = {}

def analyze():
    ctr = 0
    with open('test.log') as f:
        for line in f:
            ip = re.findall("^\d*.\d*.\d*.\d*", line)[0]
            # import pdb; pdb.set_trace();
            url = re.findall('((?:url=http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+))&params=', line)[0]
            print url
            ctr += 1
            if ctr == 10:
                break
            # if ip not in ip_adresses:
            #     ip_adresses[ip] = 1
            # else:
            #     ip_adresses[ip] += 1




if __name__ == "__main__":
    analyze()
