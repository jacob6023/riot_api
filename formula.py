# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:12:37 2022

Author: 417-DevOps
Desc: Riot API Bootcamp Module 1 example
"""

import pandas as pd
import json


with open('1641207119.json') as f:
    d = json.load(f)
    print(d)
    print(1)