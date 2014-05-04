#! /usr/bin/python
# _*_ coding: utf-8 -*-
import urllib2
#what's the defference between urllib and urllib2 ?
# stackoverflow
from lxml import etree;
def main():
    userMainUrl = 'http://www.songtaste.com/user/351979';
    req = urllib2.Request(userMainUrl);
    # request can be used to set the headers for a url
    resp = urllib2.urlopen(req)
    respHtml = resp.read();
    print 'Method 3: Use lxml to extract infoo from html'
    htmlElement = etree.HTML(respHtml);
    print 'htmlElement=',htmlElement;
    h1userElement = htmlElement.find(".//h1[@class='h1user']")
    # how to use find function ?
 
