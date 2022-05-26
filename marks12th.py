#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
from bs4 import BeautifulSoup
import json

url = 'http://cbseresults.nic.in/class12/class12th21.asp'
headers = {'Host': 'cbseresults.nic.in',
           'Referer': 'http://cbseresults.nic.in/class12/Class12th21.htm',
           'Content-Type': 'application/x-www-form-urlencoded'}

expression = 'ENGLISH'  # This should be any subject that you have eg. ENGLISH as shown on CBSE website

def brute(sch, regno):
    data = {
        'regno': regno,
        'sch': sch,
        'B2': 'Submit',
        }
    r = requests.post(url, headers=headers, data=data)
    if expression in r.text:
        return r.text


def user(regno):
    words = [w.strip() for w in open('schoolcode.txt', 'rb').readlines()]
    for word in words:
        word = word.decode('utf-8')
        sch = word
        print(sch)
        content = brute(sch, regno)
        if content:
            break
    return content


def main():
    print('Starting')
    roll = str(sys.argv[1]).strip()
    print(roll)
    c = user(roll)
    if c:
        soup = BeautifulSoup(c, 'html.parser')
        text = soup.get_text()
        text = text[text.find('Roll No:'
                              ):text.find('Check Another Result')]
        print(text.rstrip('\n').replace('  ', ''))
    else:
        print('Could not find score(An error may have occurred, Please try again)')
    X=input()


if __name__ == '__main__':
    main()
