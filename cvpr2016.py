#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2
import re
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
def download_file(download_url,file_name):
    response = urllib2.urlopen(download_url)
    file = open(file_name, 'w')
    file.write(response.read())
    file.close()
    print("Completed")
save_path = '/home/sherwood/cvpr2016/'
url = 'http://www.cv-foundation.org/openaccess/CVPR2016.py'
html = getHtml(url)
parttern = re.compile(r'\bcontent_cvpr_2016.*paper\.pdf\b')
url_list = parttern.findall(html)
for url in url_list:
    name = url.split('/')[-1]
    file_name = save_path + name
    download_file('http://www.cv-foundation.org/openaccess/'+url,file_name)



