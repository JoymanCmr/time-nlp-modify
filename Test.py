#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 10:21
# @Author  : zhm
# @File    : Test.py
# @Software: PyCharm
# @Changed : tianyuningmou
import re

import arrow

from aiml_sinitek.ducklingAnylizer import Duckling
from time_nlu.TimeNormalizer import TimeNormalizer  # 引入包

tn = TimeNormalizer()

# res = tn.parse(target='2019年度，建筑安装收入占比最高的三家公司是哪几家')
# print(res['value'][0:4])
# res = tn.parse(target='2017年一季度')
# print(res)
# res = tn.parse(target='2017年度')
# print(res)
# res = tn.parse(target='上周')
# print(res)
# res = tn.parse(target='上周二')
# print(res)
# res = tn.parse(target='下下周')
# print(res)
# res = tn.parse(target='本周')
# print(res)
# res = tn.parse(target='这周二')
# print(res)
# res = tn.parse(target='下下周二')
# print(res)
# res = tn.parse(target='查国轩高科2017年五月份的报告')
# print(res)
res = tn.parse(target='2019年 六月二十号的客户')
print(res)
# res = tn.parse(target='前两周')
# print(res)

# while True:
#     str = input("time:>")
#     print("duckling: " + duckling.parse(str, dimensions=['time']))
#     print("tn: %s " % tn.parse(target=str))

# import pickle
# # # #
# with open('./time_nlu/resource/regex.txt', 'r') as f1, open('./time_nlu/resource/regex.pkl', 'wb') as f2:
#     text = f1.read()
#     pickle.dump(re.compile(text), f2)
# #
# text = '两周前'
#
# with open('./resource/regex.pkl', 'rb') as f:
#     pattern = pickle.load(f)
#
#
#
# pattern = re.compile(r'(?<=前)\d+(?=(个)?(周|星期|礼拜)(?![以之]?[前后]))')
# match = pattern.finditer('前2周')
# for m in match:
#     print(m.group())

