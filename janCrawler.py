#!/usr/bin/env python
# encoding: utf-8

import requests
from bs4 import BeautifulSoup
import time
import os


debug = True#Whether to output the log
total_img_collections = {}
header = {'User-Agent':
          'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML,\
          like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
          }

def log(message):
    if debug == True:
        print message

def mkdirs(page):
    path = page
    exist = os.path.isdir(path)
    if not exist:
        os.mkdir(path)
    current_path = os.path.abspath(path) + '/'
    return current_path

def getUrlList(base_url,index):
    try:
        req = requests.get(base_url,timeout=10,headers=header)
    except requests.exceptions.RequestException as e:
        print e
        time.sleep(3)
    response = req.text
    soup = BeautifulSoup(response,'lxml')
    img_url_list = soup.select('div > div > div.text > p > a[target="_blank"]')
    for img_url in img_url_list:
        img = 'http:' + img_url.get('href')
        total_img_collections[index].append(str(img))
    return total_img_collections

def Download(index):
    log( 'now we crawling '+index)
    save_dir = mkdirs(index)#storage directory
    conuts = 1#picture number
    urls = total_img_collections[index]
    for url in urls:
        try:
            req = requests.get(url,headers=header,timeout=10)
        except requests.exceptions.RequestException as e:
            print e
            continue
            time.sleep(3)
        response = req.content
        #suffix_name = '.'+url.split('.')[-1]#get the suffix name of image
        suffix_name = url.split('/')[-1]#get the suffix name of image
        storage_path = save_dir + str(conuts) + suffix_name
        with open(storage_path,'wb') as f:
            f.write(response)
        log('Download %s,img%d'%(index,conuts))
        conuts += 1

def main():
    start = time.time()
    start_page = int(raw_input('What is th number of page you want to start? '))
    end_page = int(raw_input('What is th number of page you want to end? '))
    while end_page < start_page:
        print 'wrong input,the start is over the end.Try again please'
        start_page = int(raw_input('What is th number of page you want to start? '))
        end_page = int(raw_input('What is th number of page you want to end? '))
    for i in range(start_page,end_page+1):
        URL = 'http://jandan.net/ooxx/page-'
        base_url = URL + str(i)
        index = 'page%d' % i
        total_img_collections[index] = []
        #log('Crawling in page %d....' % i)
        getUrlList(base_url,index)
        Download(index)
        time.sleep(3)
    end = time.time()
    log('we all spend '+str(end-start) + ' seconds to crawl %d pages'%(end_page-start_page+1))

if __name__=='__main__':
    main()
