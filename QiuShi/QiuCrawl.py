#!/usr/bin/env python
# encoding: utf-8

import time
import codecs
import requests
from bs4 import BeautifulSoup
from readqiushi import Read


'''One small script to crawl the jokes(in the form of text) from http://qiushibaike.com/'''

def crawl_joke_list_bs4(page=1):
    url = "http://qiushibaike.com/8hr/page/" + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    joke_list = soup.find_all("div",class_="article block untagged mb15")
    for child in joke_list:
        joke_user = child.find('h2').string
        joke_content = ''.join(child.find('div',class_='content').stripped_strings)#remove extra spaces
        comp_joke = joke_user + '\t' + joke_content + '\n'
        with codecs.open('qiushibaike.txt','a','utf-8') as f:
            f.write(comp_joke)
    time.sleep(1)

if __name__ == '__main__':
    start = time.time()
    start_num = int(raw_input('start with?: '))
    end_num = int(raw_input('end with?: '))
    for i in range(start_num,end_num+1):
        print 'Now we crawling page: ' + str(i)
        crawl_joke_list_bs4(i)

    end = time.time()
    print 'we spend all: ' + str(end - start) + ' seconds'
    continue_read = raw_input('would you like to read the jokes we have just crawled? (y(Enter)/n)')
    if not continue_read.lower() == 'n':
        Read()
    else:
        exit()

