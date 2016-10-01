#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import requests
import json
import shutil

class config:

    # User Information
    @staticmethod
    def id():
        return str(config.get("id"))

    @staticmethod
    def tickets():
        return int(config.get("tickets"))

    @staticmethod
    def date():
        return str(config.get("date"))

    # Train Information
    @staticmethod
    def trainNum():
        return int(config.get("num"))

    @staticmethod
    def trainFrom():
        return int(config.get("from"))

    @staticmethod
    def trainTo():
        return int(config.get("to"))

    # Server Information
    @staticmethod
    def pageOrder():
        return str(config.get("order"))

    @staticmethod
    def pageRef():
        return str(config.get("referer"))

    @staticmethod
    def pageImg(): 
        return str(config.get("img"))

    # get Function
    @staticmethod
    def get(key):
        with open('setting.json') as dataJson:
            settings = json.load(dataJson)[0]

        return settings[key]


class RailPy:
    def __init__(self):
        self.session = requests.Session()
        print("Start Session")
        print(self.session)

    def getCode(self):
        session = self.session
        
        getImg = session.post(config.pageImg(), stream = True)
        with open('code.jpg', 'wb') as out_file:
            shutil.copyfileobj(getImg.raw, out_file)
        del getImg

    def getTickets(self,code):
        with open('setting.json') as dataJson:
            datas = json.load(dataJson)
        
        headers = datas[1]
        data = datas[2]
        datas[1]["randInput"] = code
        
        session = self.session  
        getTickets = session.get(config.pageOrder(), params = data, headers = headers)
        getTickets.encoding = "Big5"
        print(getTickets.text)

a = RailPy()
a.getCode()
code = input("code:")
a.getTickets(code)
#print(config.pageUrl())