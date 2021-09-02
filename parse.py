#env/bin/python3.9
#-*- coding:utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup


class Parse():

    debug = "parse_log.txt"


    def docs() -> None:
        print(\
            """
Parse Tool
            """)
        exit()


    def log(cause, content) -> None:
        print(f"[{time.ctime()}][{cause}]\n---\n{content}\n---\n", \
                file=open(self.debug, "a+", encoding="utf-8"))


    def __init__(self, sitename: str or list, auth: list or dict, method: str or dict,\
                    attr="", infinity=False, interval=False) -> None:
        self.URI = sitename
        self.AUTH = auth
        self.METHOD = method
        self.ATTR = attr
        self.INFINITY = infinity
        self.INTERVAL = interval


    def get(self, arg):
        args = [self.URI, self.AUTH, self.METHOD, self.ATTR, self.INFINITY, self.INTERVAL]
        call_arg = {
            "all": args,
            "url": self.URI,
            "auth": self.AUTH,
            "method": self.METHOD,
            "attr": self.ATTR,
            "infinity": self.INFINITY,
            "interval": self.INTERVAL,
            }
        return call_arg[arg]


    def post(self, arg, value):
        call_arg = {
            "url": 0,
            "auth": 1,
            "method": 2,
            "attr": 3,
            "infinity": 4,
            "interval": 5,
            }
        args = [self.URI, self.AUTH, self.METHOD, self.ATTR, self.INFINITY, self.INTERVAL]
        args[call_arg[arg]] = value
        return args


    def parse(self):
        try:
            if self.AUTH:
                status = requests.get(self.URI, self.AUTH).status()
                if status == 200:
                    text = requests.get(self.URI, self.AUTH).text
                    return text
                else:
                    self.log("Error!", "Invalid status -> {}".format(status))
            else:
                status = requests.get(self.URI).status()
                if status == 200:
                    text = requests.get(self.URI).text
                    return text
                else:
                    self.log("Error!", "Invalid status -> {}".format(status))
        except Exception as err:
            self.log("Error!", "GET Exception -> {}".format(err))


    def gen(self, data: str):
        try:
            content = BeautifulSoup(data)
            return content
        except Exception as err:
            self.log("Error!", "format() -> Invalid data -> {}".format(err))


    def main(self):
        install = self.parse()
        content = self.gen(install)
        return content
