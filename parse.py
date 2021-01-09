#usr/bin/env python
#-*- coding: utf-8 -*-

import requests as req

print("1. *Введите URL.")
print("2. *Введите имя папки.")
parseMethod = str(input())

def parseUrl():
	print("В каком расширении сохранить спарсенную страницу? *Пример: html или txt, писать расширение без точки.")
	code = str(input(": "))
	parseUrl = str(input("URL: "))
	isHttp = "https://"

	if isHttp in parseUrl:
		pass

	else:
		parseUrl = str(isHttp) + str(parseUrl)

	r = req.get("%s" % parseUrl)
	parseHtmlElements(r, code)

def parseUrlFromFile():
	print("В каком расширении сохранить спарсенную страницу? *Пример: html или txt, писать расширение без точки.")
	code = str(input(": "))
	parseUrlsInFile = str(input("File name: "))
	parseUrlsList = []
	fileOpen = open("%s" % parseUrlsInFile, "r")
	fileRead = fileOpen.read()
	parseUrlsList = fileRead.split(" ")
	parseUrlsList = [line.rstrip("\n") for line in parseUrlsList] 
	fileOpen.close()
	n = 0
	for link in parseUrlsList:
		n += 1
		r = req.get(link)
		parseMoreHtmlElements(r, n, code)


def parseHtmlElements(a, b):
	fileOpen = open("parseHtmlPage.%s" % b, "w")
	fileOpen.write(a.text)
	fileOpen.close()

def parseMoreHtmlElements(a, b, c):
	fileOpen = open("parseHtmlPage%s.%s" % (b, c), "w")
	fileOpen.write(a.text)
	fileOpen.close()

if parseMethod == "1":
	parseUrl()

elif parseMethod == "2":
	parseUrlFromFile()

else:
	print("Error: " + parseMethod + "Нет такого метода.")