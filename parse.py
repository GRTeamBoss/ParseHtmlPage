#usr/bin/env python
#-*- coding: utf-8 -*-

import requests as req


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
                            data_find[1].append([
                                f'{temp_data_tag[1][num]}', 
                                f'{" ".join(data[temp_data_tag[0][num][0]+1:temp_data_tag[0][num+1][0]])}' if 
                                int(temp_data_tag[0][num+1][0]-temp_data_tag[0][num][0]+1) > 0 else ' ', 
                                f'{temp_data_tag[1][num+1]}'
                            ])
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


        # FIND CLASS
        def find_class(self, data: list, className: str | list) -> list:
            data_find = list()
            data_class = list()
            data_class_list = list()
            for num in range(2):
                data_class.append(list())
                data_find.append(list())
            if type(className) == str:
                for num in range(len(data)):
                    if className in data[num]:
                        data_class[0].append(num)
                        data_class[1].append(data[num])
                LIMIT = len(data_class)//2
                temp_data_class = list(data_class)
                while len(data_find[1]) < LIMIT:
                    for num in range(len(temp_data_class[0])):
                        data_find[0].append(temp_data_class[0][num])
                        data_find[1].append(temp_data_class[1][num])
                for num in range(len(data_find[1])):
                    if num > 0:
                        for iteration in range(num):
                            if data_find[0][num][0] < data_find[0][iteration][0]:
                                data_find[0].insert(iteration, data_find[0][num])
                                data_find[0].pop(num+1)
                                data_find[1].insert(iteration, data_find[1][num])
                                data_find[1].pop(num+1)
                return data_find[1]
            elif type(className) == list:
                for name in className:
                    data_class[0].clear()
                    data_class[1].clear()
                    
                    for num in range(len(data)):
                        if name in data[num]:
                            data_class[0].append(num)
                            data_class[1].append(data[num])
                    LIMIT = len(data_class[0])

                    while len(data_find[1]) < LIMIT:
                        for num in range(len(data_class[0])):
                            data_find[0].append(data_class[0][num])
                            data_find[1].append(data_class[1][num]

                    for num in range(len(data_class[0])):
                        if num > 0:
                            for iteration in range(num):
                                if data_find[0][num][0] < data_find[0][iteration][0]:
                                    data_find[0].insert(iteration, data_find[0][num])
                                    data_find[0].pop(num+1)
                                    data_find[1].insert(iteration, data_find[1][num])
                                    data_find[1].pop(num+1)
                    data_class_list.append([data_find[0], data_find[1]])
            
                if len(data_class_list) > 1:
                    count_class = 0
                    result = list()
                    success = list()
                    success = [[]]*(len(className))
                    for num in range(len(success)):
                        success[num] = [[]]*2
                    for num in range(len(success)):
                        success[num][0] = [[]]*(len(max(data_class_list)))
                        success[num][1] = [[]]*(len(max(data_class_list)))
                    for elem in className:
                        for path in range(len(data_class_list)):
                            for element in range(len(data_class_list[path][1])):
                                if elem in data_class_list[path][1][element]:
                                    success[count_class][0][element] = data_class_list[path][0][element]
                                    success[count_class][1][element] = data_class_list[path][1][element]
                        count_class += 1
                    for num in range(len(data)):
                        for count in range(len(succes)):
                            for elem in range(len(success[count][0])):
                                if num == success[count][0][elem]:
                                    if num in check_success:
                                        check_success[num] += 1
                                    else:
                                        check_success[num] = 1
                    for key, value in check_success:
                        if len(className) == value:
                            result.append(data[value])
                    return result
                else:
                    return "Please give me <str class>"



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

parse = Parse()
data = parse.call_method(method=1, link="https://instagram.com/gr_team_boss/?__a=1")
class_parse = Parse.find_class(data=data, className="btn")
print(class_parse)
