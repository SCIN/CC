#!/usr/bin/env python
import sys
import os

#namespaces are all in lower cases
namespacesBlacklist = ['draft talk', 'draft', 'gadget talk', 'gadget', 'gadget definition talk', 'gadget definition', 'talk', 'user talk', 'user', 'wikipedia talk', 'wikipedia', 'file talk', 'file', 'mediawiki talk', 'mediawiki', 'topic', 'education program talk', 'education program', 'timedtext talk', 'timedtext', 'book', 'book talk', 'portal', 'portal talk', 'template talk', 'template', 'help talk', 'help', 'category talk', 'category', 'module talk', 'special', 'module', 'media']

filesuffixBlacklist = ['.png','.gif','.jpg','.jpeg','.tiff','.tif','.xcf','.mid','.ogg','.ogv','.svg','.djvu','.oga','.flac','.opus','.wav','.webm','.ico','.txt']
boilerplateBlacklist = ['404_error/','Main_Page','Hypertext_Transfer_Protocol','Search']

def linefilter(line):
	splitList = line.split(" ")
	while '' in splitList:
		splitList.remove('')
	judge = 0
	while 1:
		# rule 1
		if len(splitList) != 4:
			judge = 1
			break
		#rule 2
		if splitList[0] != "en" and splitList[0] != "en.m":
			judge = 1
			break
		# rule 3 4
		if splitList[1].find(':') != -1 or splitList[1].lower().find('%3a') != -1:
			for i in range(len(namespacesBlacklist)):
				if splitList[1].lower().startswith(namespacesBlacklist[i]) or splitList[1].lower().replace('_',' ').startswith(namespacesBlacklist[i])  or splitList[1].lower().replace('%3a',' ').startswith(namespacesBlacklist[i]) : #case insensitive
					leng = len(namespacesBlacklist[i])
					if splitList[1][leng] == ':' or splitList[1][leng : leng + 3].lower() == '%3a':
						judge = 1
						break
			if judge == 1:
				break
		# rule 5
		if splitList[1][0].islower():
			judge = 1
			break
		# rule 6
		if splitList[1].find('.') != -1:
			lowerTitle = splitList[1].lower()
			for i in filesuffixBlacklist:
				if lowerTitle.endswith(i):
					judge = 1
					break
			if judge == 1:
				break
		# rule 7
		for i in boilerplateBlacklist:
			if splitList[1] == i:
				judge = 1
				break
		break

	if judge == 1:
		return ""
	else:
		return (splitList[1] + '\t' + splitList[2])


for line in sys.stdin:
	line = line.strip()
	result = linefilter(line)
	for word in words:


