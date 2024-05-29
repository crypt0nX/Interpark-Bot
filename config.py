#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 
# @Time    : 2024/5/18 23:29
# @File    : config.py
# @annotation    :


GOODS_ID = '24007162'
TIME = '20240707'


BizMemberCode = None

INITIAL_URL = f'https://www.globalinterpark.com/en/product/{GOODS_ID}'


def getInitialUrl(BizMemberCode):
    INITIAL_URL2 = ('https://gpoticket.globalinterpark.com/Global/Play/Booking/BookingSessionGate.asp?'
                    f'v1={GOODS_ID}&'
                    'v2=G2001&'
                    f'v3={TIME}&'
                    f'v4=001&v5=N&v6=10965&v7={BizMemberCode}&v8=N')
    return INITIAL_URL2
