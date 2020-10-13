# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:27:25 2020

@author: mickj
"""

import requests

rq = requests.get('http://localhost:8081/showAll')


print(rq.text)