#usr/bin/env python
#-*- coding: utf-8 -*-

import asyncio as aio

import requests as req
import websockets as web


__all__ = (aio.__all__)

class Parse:

	URI = 'https://www.'
	WSS_URI = 'wss://www.'
	WEB_CALL = web

	# CONSTRUCTOR
	def __init__(self, GET_MODE='text') -> None:

		self.GET_MODE = GET_MODE


	def call_method(self, method: str, link: str) -> list:

		callback_function = {
			'1': self.get_URL_content,
			'2': self.get_PATH_content,
			'3': self.get_WSS_content,
		}
		return callback_function[method](url=link)

	# CONTENT_MODIFY
	def content_modify(self, arg) -> list:
		data_modify = list()

		for el in arg:
			data_modify.append(el.lstrip().rstrip())

		return data_modify

	# FIND_TAG
	def find_tag(self, data: list, tag: str) -> list:
		data_tag = list()
		for num in range(2):
			data_tag.append(list())
		data_find = list()
		count_start = int()
		count_end = int()
		if bool(filter(lambda elem: f'<{tag}' in elem, data)):
			for element in data:
				if any((f'{tag}' in element, f'/{tag}' in element)):
					data_tag[0].append([
						data.index(element),
						f'start{count_start}' if f'{tag}' in element and
						f'/{tag}' not in element else f'end{count_end}'
					])
					data_tag[1].append(f'{element}>')
					if f'{tag}' in element and f'/{tag}' not in element:
						count_start += 1
					if f'/{tag}' in element:
						count_end += 1
			count = 1
			while len(data_find) < len(data_tag[1])//2:
				for num in range(len(data_tag[0])):
					if num < len(data_tag[0])-count:
						_now = data_tag[0][num][1]
						_next = data_tag[0][num+count][1]
						if 'start' in _now and 'end' in _next:
							data_find.append([f'{data_tag[1][num]}', f'{data_tag[1][num+count]}'])
				count += 1
			return data_find
		else:
			return 'This tag not found!'


	# GET_URL_CONTENT
	def get_URL_content(self, url) -> list:

		RESPONSE = req.get(f'{self.URI}{url}')
		MODE = {
			'text': RESPONSE.text,
			'content': RESPONSE.content,
		}

		data = MODE[self.GET_MODE].rstrip().split('>')
		data_modified = self.content_modify(arg=data)
		return data_modified

	# GET_PATH_CONTENT
	def get_PATH_content(self, path) -> list:

		with open(f'{path}', 'r', encoding='utf-8') as file:
			RESPONSE = file.read()

		data = RESPONSE.rstrip().split('>')
		data_modified = self.content_modify(arg=data)
		return data_modified


	async def get_WSS_content(self, url) -> list:
		web_connect = self.WEB_CALL.connect(f'{self.WSS_URI}{url}')
		data = web_connect.recv().rstrip().split('>')
		data_modified = self.content_modify(arg=data)
		web_connect.close()
		return data_modified
		
		
		




parse = Parse().call_method('3', 'instagram.com/gr_team_boss/?__a=1')
# tag = Parse().find_tag(parse, 'div')
print(parse)
