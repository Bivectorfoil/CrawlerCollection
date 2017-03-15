#!/usr/bin/env python
# encoding: utf-8

'''A script to read file qiushibaike.txt'''


def con_read(f,page=6):
    for i in range(1,page+1):
        print f.readline()
    return

def Read():

    try:
        f = open('qiushibaike.txt')
    except IOError,e:
        print e
        print 'please check the directory if there is such file'
        exit()
    read_continue = True
    page = raw_input('How much jokes do you want to read once?(default=6): ')
    if page == '':
        page = 6
    else:
        page = int(page)

    while read_continue:
        flag = raw_input('continue reading?(y(Enter)/n) ')
        if flag != 'n':
            con_read(f,page)
        else:
            f.close()
            read_continue = False

if __name__ == '__main__':
    Read()
