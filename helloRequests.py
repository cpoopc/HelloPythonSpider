# -*- coding: utf-8 -*-
# 声明编码格式 https://www.python.org/dev/peps/pep-0263/

import requests

def testRequests(url,params = None):
    rq = requests.get(url,params);
    if(rq.status_code == 200):
        print "请求成功"
    elif(rq.status_code == 500):
        print "code 500"
    else:print("code:"+str(rq.status_code))
    # print rq.content
    print rq.encoding
    print rq.text

if __name__ == '__main__':
    # url_1 = "http://docs.python-requests.org/en/master/"
    url_http_get = "http://httpbin.org/get"
    # # url_http_post = "http://httpbin.org/post"
    # url_github_timeline = "https://github.com/timeline.json"
    testRequests(url_http_get)