#env/bin/python3.9
#-*- coding:utf-8 -*-

import requests
import time


class Parse():


    def docs() -> None:
        print(\
            """
Parse Tool
            """)
        exit()


    def log(cause, content) -> None:
        print(f"[{time.ctime()}][{cause}]\n---\n{content}\n---\n", \
                file=open("parse_log.txt"))


    def __init__(self, sitename: str or list, auth: dict, method: str or dict,\
                    infinity=False, interval=False) -> None:
        self.URI = sitename
        self.AUTH = auth
        self.METHOD = method
        self.ATTR = False
        self.INFINITY = infinity
        self.INTERVAL = interval


    def get():
        pass


    def post():
        pass


    def attr(self, filename: str):
        with open(filename, "r", encoding="utf-8") as file:
            buffer = file.read().split("/;")
        self.ATTR = buffer


    def cycle(self):
        URI_type = type(self.URI)
        METHOD_type = type(self.METHOD)
        if METHOD_type == str:
            pass
        elif METHOD_type == dict:
            pass
        else:
            self.log("Error", "Incorrect <method> type")
            return "Error! Please watch parse_log.txt"