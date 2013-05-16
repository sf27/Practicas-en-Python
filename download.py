#!/usr/bin python
#-*-coding:utf-8-*-
import sys, os
def wget(url):
	os.system("wget " + url)

for url in sys.argv[1:]:
	print url
	print wget(url)
	


