#!/usr/bin/env python3

import feedparser
import time
import microdotphat

# initial flashing NEWS
for i in range (5):
    microdotphat.fill(1)
    microdotphat.show()
    time.sleep(0.1) 
    microdotphat.clear()
    microdotphat.show()
    time.sleep(0.1) 
    microdotphat.write_string('NEWS',kerning=False)
    microdotphat.show()
    time.sleep(0.1)
    microdotphat.clear()
    microdotphat.show()
    time.sleep(0.1)

# main section of the code
newsfeed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")

headlines = []

for i in range(5):
    headlines.append(newsfeed['entries'][i]['title'])
    headlines.append("        ")
    print (headlines)
    news = ''.join([str(item) for item in headlines])
    news.replace('-',' ')
    news.replace('%',' percent')
    news.replace('£',' GBP')
    characters = (len(news))
    microdotphat.write_string(news,offset_x=0,kerning=False)

for i in range ((characters+16)*8):
    microdotphat.scroll()
    microdotphat.show()
    time.sleep(0.01) 
