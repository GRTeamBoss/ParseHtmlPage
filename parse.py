#usr/bin/env python
#-*- coding: utf-8 -*-

import asyncio as aio

import requests as req
import websockets


class Parse:

        URI = 'https://www.'
        WSS_URI = 'wss://'

        # CONSTRUCTOR
        def __init__(self, GET_MODE='text') -> None:

                self.GET_MODE = GET_MODE


        def call_method(self, method: str, link: str) -> list:

                callback_function = {
                        '1': self.get_URL_content,
                        '2': self.get_PATH_content,
                }
                return callback_function[method](url=link)

        # CONTENT_MODIFY
        def content_modify(self, arg) -> list:
                data_modify = list()
                for el in arg:
                        if '<' in el:
                                data_modify.append(f'{el.lstrip().rstrip()}>')
                        elif any((el in str(), '\n' in el, '\t' in el)):
                                continue
                        else:
                                data_modify.append(el.lstrip().rstrip())
                return data_modify

        # FIND_TAG
        def find_tag(self, data: list, tag: str) -> list:
                data_tag = list()
                for num in range(2):
                        data_tag.append(list())
                data_find = list()
                for num in range(2):
                        data_find.append(list())
                count_start = int()
                count_end = int()
                if all((f'{tag}' in data, f'/{tag}' in data)):                       
                        for num in range(len(data)):
                                if any((f'{tag}' in data[num], f'/{tag}' in data[num])):
                                        data_tag[0].append([
                                                num,
                                                f'end{count_end}' if f'/{tag}' in data[num] else f'start{count_start}'
                                        ])
                                        data_tag[1].append(data[num])
                                        if f'/{tag}' in data[num]:
                                                count_end += 1
                                        else:
                                                count_start += 1
                        LIMIT = len(data_tag[0])//2
                        temp_data_tag = list(data_tag)
                        while len(data_find[1]) < LIMIT:
                                for num in range(len(temp_data_tag[0])):
                                        if num < len(temp_data_tag[0])-1:
                                                now_ = temp_data_tag[0][num][1]
                                                next_ = temp_data_tag[0][num+1][1]
                                                if all(('start' in now_,'end' in next_)):
                                                        data_find[0].append([temp_data_tag[0][num][0], temp_data_tag[0][num+1][0]])
                                                        data_find[1].append([f'{temp_data_tag[1][num]}', f'{" ".join(data[temp_data_tag[0][num][0]+1:temp_data_tag[0][num+1][0]])}' if int(temp_data_tag[0][num+1][0]-temp_data_tag[0][num][0]+1) > 0 else ' ', f'{temp_data_tag[1][num+1]}'])
                                                        temp_data_tag[0].pop(num+1)
                                                        temp_data_tag[0].pop(num)
                                                        temp_data_tag[1].pop(num+1)
                                                        temp_data_tag[1].pop(num)
                        for num in range(len(data_find[1])):
                                if num > 0:
                                        for iteration in range(num):
                                                if data_find[0][num][0] < data_find[0][iteration][0]:
                                                        data_find[0].insert(iteration, data_find[0][num])
                                                        data_find[0].pop(num+1)
                                                        data_find[1].insert(iteration, data_find[1][num])
                                                        data_find[1].pop(num+1)
                        return data_find[1]
                elif f'{tag}' in data:
                        for num in range(len(data)):
                                if f'{tag}' in data[num]:
                                        data_find[0].append(num)
                                        data_find[1].append(data[num])
                        for num in range(len(data_find[1])):
                                if num > 0:
                                        for iteration in range(num):
                                                if data_find[0][num][0] < data_find[0][iteration][0]:
                                                        data_find[0].insert(iteration, data_find[0][num])
                                                        data_find[0].pop(num+1)
                                                        data_find[1].insert(iteration, data_find[1][num])
                                                        data_find[1].pop(num+1)
                        return data_find[1]
                                                
                else:
                        return f"This tag -> '{tag}' not found!"


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

parse = Parse().call_method('1', 'instagram.com/gr_team_boss/?__a=1')
tag = Parse().find_tag(parse, 'hr')
print(tag)
