#usr/bin/env python
#-*- coding: utf-8 -*-

from os import link
import requests as req

class Parse:


	URI = 'https://www.'

    #  CONSTRUCTOR
	def __init__(self, GET_MODE = 'text') -> None:

		self.GET_MODE = GET_MODE


	def call_method(self, method: str, link: str) -> list:

		callback_function = {
			'1': self.get_URL_content,
			'2': self.get_PATH_content,
		}
		return callback_function[method](url = link)

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
		data_find_dict = dict()
		tree = dict()

		if any( ( filter(lambda elem: f'<{tag}>' in elem, data), filter(lambda elem: f'<{tag}' in elem, data) ) ):

			if bool(filter(lambda elem: f'</{tag}>' in elem, data)) == False:

				try:

					for num in range(len(data)):

						if f'<{tag}' in data[num]:
							data_tag[0].append(num)
							data_tag[1].append(data[num])

					for num in range(len(data_tag[0])):

						data_find.append(f'{data[int(data_tag[0][num])]}>')
						data_find_dict[str(data_tag[0][num])] = f'{data[int(data_tag[0][num])]}>'
					return data_find

				except Exception as e:
					return e

			else:

				try:

					for num in range(len(data)):

						if any(( f'<{tag}' in data[num], f'</{tag}' in data[num] )):
							data_tag[0].append(num)
							data_tag[1].append(data[num])

					for num in range(len(data_tag[0])):

						# data_find.append(f'{data[int(data_tag[0][num])]}>')
						data_find_dict[str(data_tag[0][num])] = f'{data[int(data_tag[0][num])]}>'

					_temp_key = list()
					def sort(data: dict, tree: dict, count: list, content: list) -> dict:
						for key, value in data_find_dict.items():
							if f'<{tag}' in value:
								for keys in data_find_dict:
									if f'</{tag}' in data[keys] \
										and list(data.values()).index(data[keys]) - list(data.values()).index(value) >= 1 \
										and len(list(filter(lambda elem: keys == elem, count))) == 0 \
										and len(list(filter(lambda elem: key == elem, tree))) == 0:
										tree[key] = f'{value} {"> ".join(content[int(key)+1 : int(keys)])}> {data[keys]}'
										count.append(keys)
						return tree
					result = sort(data_find_dict, tree, _temp_key, data)
					
					# data_start = list(filter(lambda elem: f'<{tag}' in elem or f'<{tag}>' in elem, data_find))
					# data_end = list(filter(lambda elem: f'</{tag}>' in elem, data_find))
					return result

				except Exception as e:
					return e
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
		data_modified = self.content_modify(arg = data)
		return data_modified

    # GET_PATH_CONTENT
	def get_PATH_content(self, path) -> list:

		with open(f'{path}', 'r', encoding='utf-8') as file:
			RESPONSE = file.read()

		data = RESPONSE.rstrip().split('\n')
		data_modified = self.content_modify(arg = data)
		return data_modified




parse = Parse().call_method('1', 'instagram.com/gr_team_boss/?__a=1')
# print(parse)
tag = Parse().find_tag(parse, 'div')
print(tag)