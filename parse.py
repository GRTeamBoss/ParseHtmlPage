#usr/bin/env python
#-*- coding: utf-8 -*-

import requests as req

class Parse:
	"""
	Documentation:
	Example:

	-----------------------------
	| Parse(method, link, type) |
	-----------------------------
	
	--------
	method:
	1. URL
	2. file:///PATH/to/folder
	*INPUT ONLY NUMBER IN STRING FORMAT
	--------
	link:
	- file:///PATH/to/folder/filename
	- C:/PATH/to/folder/filename
	- /path/to/folder/filename
	----
	- https://site.type
	- site.type
	--------
	type:
	- txt
	- html
	- php
	- py
	- and other
	*INPUT WITHOUT '.'(DOT)
	"""

	def __init__(self, method, link, format):

		if method == "1":
			self.parseUrl(link, format)

		elif method == "2":
			self.parseUrlFromFile(link, format)

		else:
			self.out(str("Error: " + method + "Нет такого метода."))


	def docs():
		info = """
			Documentation:
			Example:

			-----------------------------
			| Parse(method, link, type) |
			-----------------------------
			
			--------
			method:
			1. URL
			2. file:///PATH/to/folder
			*INPUT ONLY NUMBER
			--------
			link:
			- file:///PATH/to/folder
			- C:/PATH/to/folder
			- /path/to/folder
			----
			- https://site.type
			- site.type
			--------
			type:
			- txt
			- html
			- php
			- py
			- and other
			*INPUT WITHOUT '.'(DOT)
				"""
		return info	


	def out(self, content):
		return content


	def parseUrl(self, url, format):
		code = format
		parseUrl = url
		isHttp = "https://"

		if isHttp in parseUrl != True:
			parseUrl = str(isHttp) + str(parseUrl)

		r = req.get("%s" % parseUrl)
		self.parseHtmlElements(r, code)


	def parseUrlFromFile(self, url, format):
		code = format
		parseUrlsInFile = url
		parseUrlsList = list()
		with open("%s" % parseUrlsInFile, "r") as fileOpen:
			fileRead = fileOpen.read()
			parseUrlsList = fileRead.split(" ")
			parseUrlsList = [line.rstrip("\n") for line in parseUrlsList] 
		n = 0
		for link in parseUrlsList:
			n += 1
			r = req.get(link)
			self.parseMoreHtmlElements(r, n, code)


	def parseHtmlElements(self, a, b):
		with open("parseHtmlPage.%s" % b, "w", encoding='utf-8') as fileOpen:
			fileOpen.write(a.text)

	def parseMoreHtmlElements(self, a, b, c):
		with open("parseHtmlPage%s.%s" % (b, c), "a", encoding='utf-8') as fileOpen:
			fileOpen.write(a.text)

print(Parse.docs())