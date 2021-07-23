#usr/bin/env python
#-*- coding: utf-8 -*-

import requests as req

class Parse:


	URI = 'https://www.'


	def __init__(self, method: str, link: str, EXTENSION = 'txt', GET_MODE = 'text', GET_ARGS = '') -> None:

		self.EXTENSION = EXTENSION
		self.GET_MODE = GET_MODE
		self.GET_ARGS = GET_ARGS

		callback_function = {
			'1': self.get_URL_content,
			'2': '',
		}
		callback_function[method](link)


	def content_modify(self, arg):
		data_modify = list()
		for el in arg:
			data_modify.append(el.lstrip().rstrip())
		return data_modify


	def find_component(self, data):
		if self.GET_ARGS == '':
			result = '\n'.join(data)
			return result
		if type(self.GET_ARGS) == type(str()):
			pass
		if type(self.GET_ARGS) == type(list()):
			args_tag = filter(lambda tag: '#' not in tag and '.' not in tag, self.GET_ARGS)
			args_starts_lattice = filter(lambda lattice: lattice.startswith('#'), self.GET_ARGS)
			args_starts_dote = filter(lambda dote: dote.startswith('.'), self.GET_ARGS)
			
			
	

	def find_tag(self):
		data_start_tag = list()
		data_end_tag = list()

		try:
			for i in data:
				if any((f'<{self.GET_ARGS}>', f'<{self.GET_ARGS}')) in i:
					data_start_tag.append(i)
				if f'</{self.GET_ARGS}>' in i:
					data_end_tag.append(i)

		except Exception as e:
			pass


	def get_URL_content(self, url):
		RESPONSE = req.get(f'{self.URI}{url}')
		MODE = {
			'text': RESPONSE.text,
			'content': RESPONSE.content,
		}
		data = MODE[self.GET_MODE].rstrip().split('\n')
		data_modified = self.content_modify(arg = data)
		return data_modified




Parse('1', 'instagram.com/gr_team_boss/?__a=1')