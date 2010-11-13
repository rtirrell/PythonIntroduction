#!/usr/bin/env python

import urllib2
import re
from xml.dom import minidom, Node
from operator import itemgetter

rss_pattern = re.compile('link rel="alternate" href="(http://twitter.com/statuses/user_timeline/[0-9A-Za-z].*\.rss)"')
pubd_pattern = re.compile('..., ([0-9]+) ([A-Za-z]+) ([0-9]+) (..):(..):(..).*')

def get_rss_url(twtracct):
    urlstr = "http://www.twitter.com/" + twtracct
    htmlstr = urllib2.urlopen(urlstr).read()
    mo = rss_pattern.search(htmlstr)
    if (mo):
        return mo.group(1)
    return None

def sortable_pubdate(pubdate):
    mondict = {'Jan':'01', 'Feb':'02', 'Mar':'03',
               'Apr':'04', 'May':'05', 'Jun':'06',
               'Jul':'07', 'Aug':'08', 'Sep':'09',
               'Oct':'10', 'Nov':'11', 'Dec':'12'}
    mo = pubd_pattern.search(pubdate)
    if (mo):
        datestr = mo.group(3) + mondict[mo.group(2)] + mo.group(1)
        timestr = mo.group(4) + mo.group(5) + mo.group(6)
        return datestr + timestr
    return "00000000000000"
    
def get_tweets(username):
    rss_url = get_rss_url(username)
    lst = []
    #print 'RSS: ' + rss_url
    rss_stuff = urllib2.urlopen(rss_url)
    xmldoc = minidom.parse(rss_stuff)
    rootNode = xmldoc.documentElement
    for node in rootNode.childNodes:
        if (node.nodeName == "channel"):
            for item_node in node.childNodes:
                if item_node.nodeName == "item":
                    title = ""
                    pubdate = ""
                    for tnode in item_node.childNodes:
                        if (tnode.nodeName == "title"):
                            for text_node in tnode.childNodes:
                                if (text_node.nodeType == node.TEXT_NODE):
                                    title += text_node.nodeValue
                        if (tnode.nodeName == "pubDate"):
                            for text_node in tnode.childNodes:
                                if (text_node.nodeType == node.TEXT_NODE):
                                    pubdate += text_node.nodeValue
                    if (len(title)>0):
                        lst.append({'date':sortable_pubdate(pubdate), 'text':title})
    rss_stuff.close()
    return lst

if __name__ == '__main__':
    lst = get_tweets('cnn')
    lst.extend(get_tweets('nytimes'))
    lst.sort(key=itemgetter('date'), reverse=True);
    print '\n'.join([a['text'] for a in lst])