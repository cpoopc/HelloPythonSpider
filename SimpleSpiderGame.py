# -*- coding: utf-8 -*-
# 声明编码格式 https://www.python.org/dev/peps/pep-0263/

# import os, sys, time, platform, random
import re
import requests
# try:
#     from bs4 import BeautifulSoup
# except:
#     import BeautifulSoup

# 正则匹配字符串,找到数字
def findNumber(content):
    numberMatch = re.compile(r'(数字|数字是)(?P<number>\d+)').search(content);
    if numberMatch:
        print "找到数字"
        print numberMatch.group('number')
        return numberMatch.group('number')
    else:
        print("没有找到数字")
        return None

# 从网址中找到数字,生成新url,递归
def testGame1(url, number = None):
    if(number != None):
        finalurl = url +"/"+str(number)
    else:
        finalurl = url
    print(finalurl)
    rq = requests.get(finalurl)
    # soup = BeautifulSoup(rq.content,"html.parser");
    # soup.find()
    findNum = findNumber(rq.content)
    # findNumber("你需要在网址后输入数字79303")
    if findNum:
        testGame1(url, findNum)
    else:
        print(rq.content)

# 密码为30以下的数字,循环post账号密码直到正确
def testGame2(num):
    params = {'username':'cp',"password":str(num)}
    rq = requests.post("http://www.heibanke.com/lesson/crawler_ex01/",data=params);
    searchResult = re.compile(r'您输入的密码错误, 请重新输入').search(rq.content);
    if (searchResult and num<31):
        testGame2(num+1)
    else:
        print(num)

if __name__ == '__main__':
    testGame1("http://www.heibanke.com/lesson/crawler_ex00")
    testGame2(0)