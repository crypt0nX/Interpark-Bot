#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 
# @Time    : 2024/5/29 18:22
# @File    : auto_fill_info.py
# @annotation    :
import time


def fillPersonalInfo(tab):
    tab.ele('xpath:/html/body/form/div/div[2]/div/div[1]/table/tbody/tr[2]/td/input').input('TBD')
    tab.ele('xpath://*[@id="BirYear"]').select.by_value("TBD")
    tab.ele('xpath://*[@id="BirMonth"]').select.by_value("TBD")
    tab.ele('xpath://*[@id="BirDay"]').select.by_value("TBD")
    tab.ele('xpath:/html/body/form/div/div[2]/div/div[1]/table/tbody/tr[8]/td/input').input("TBD")
    tab.ele('xpath:/html/body/form/div/div[2]/div/div[1]/table/tbody/tr[12]/td/select').select.by_value("TBD")
    tab.ele('xpath:/html/body/form/div/div[2]/div/div[1]/table/tbody/tr[10]/td/input').input("TBD")
    tab.ele('xpath:/html/body/form/div/div[2]/div/div[1]/table/tbody/tr[12]/td/input').input("TBD")


def fillPaymentInfo(tab):
    tab.ele('xpath:/html/body/div/form/div[2]/div/div[1]/ul/div/li[2]/p/input').click()
    time.sleep(0.1)
    tab.ele('xpath:/html/body/div/form/div[2]/div/div[1]/ul/div/li[2]/p/select').select.by_value("TBD")
    tab.ele('xpath:/html/body/div/form/div[2]/div/div[1]/ul/div/li[2]/div/div/table/tbody/tr[2]/td/input[1]').input(
        "TBD")
    tab.ele('xpath:/html/body/div/form/div[2]/div/div[1]/ul/div/li[2]/div/div/table/tbody/tr[2]/td/input[2]').input(
        "TBD")
    tab.ele('xpath:/html/body/div/form/div[2]/div/div[1]/ul/div/li[2]/div/div/table/tbody/tr[2]/td/input[3]').input(
        "TBD")
    tab.ele('xpath:/html/body/div/form/div[2]/div/div[1]/ul/div/li[2]/div/div/table/tbody/tr[2]/td/input[4]').input(
        "TBD")
    tab.ele(
        'xpath:/html/body/div/form/div[2]/div/div[1]/ul/div/li[2]/div/div/table/tbody/tr[3]/td/select[1]').select.by_value(
        "TBD")
    tab.ele(
        'xpath:/html/body/div/form/div[2]/div/div[1]/ul/div/li[2]/div/div/table/tbody/tr[3]/td/select[2]').select.by_value(
        "TBD")
