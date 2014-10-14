"""
    Author: Bharadwaj Srigiriraju

    A simple log file analyzer.

"""

import re
import operator

ip_adresses = {}
page_titles = {}
urls = {}
ids = {} #TODO: implement the ids part

def insert(x, y):
    """
    Places the entities in their respective dictionaries, along with their count.
    """
    x = str(x)
    if x not in y:
        y[x] = 0
    else:
        y[x] += 1

def log_print(desc, adict):
    """
    Prints the 5 most visited desc type from their respective sorted dictionaries.
    """
    print "the 5 most visited ", desc, " are: "
    ctr = 0
    for k in adict:
        if ctr >= 5:
            break
        print adict[k]
        ctr += 1

def analyze(file_name):
    """
    Analyzes the log file and inserts the urls, titles and ips in a dictionary.
    """
    try:
        with open(file_name) as f:
            for line in f:
                    ip = re.findall("^\d*.\d*.\d*.\d*", line)[0]
                    url = re.findall('((?:url=http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+))&params=', line)[0]
                    title = re.findall('200\s*|\d*\"((http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+))\"', line)
                    t_index = len(list(title))-1
                    title = list(re.findall('200\s*|\d*\"((http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+))\"', line))[t_index]
                    t_index = len(list(title))-1
                    insert(ip, ip_adresses)
                    insert(url, urls)
                    insert(title, page_titles)
    except IOError:
        print "File not found. Please try again"
        exit()

if __name__ == "__main__":
    print "Enter the filename (put it in the same dir as script)"
    file_name = raw_input()
    analyze(file_name)
    # sort the dictionaries by value
    sorted_urls = sorted(urls.items(), key=operator.itemgetter(1))
    sorted_ips = sorted(ip_adresses.items(), key=operator.itemgetter(1))
    sorted_page_titles = sorted(page_titles.items(), key=operator.itemgetter(1))
    log_print("ip addresses", sorted_ips)
    log_print("urls", sorted_urls)
    log_print("page titles", sorted_page_titles)
