#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 
# @Time    : 2024/5/18 22:48
# @File    : main.py
# @annotation    :
import random
import time
from DrissionPage import WebPage
from utils.captcha import RecaptchaSolver
from utils.seat_filter import filter_golden_seat, find_seat
from utils.auto_fill_info import fillPersonalInfo, fillPaymentInfo
import config

driver = WebPage()
driver.post(url=config.INITIAL_URL)
for i in driver.cookies():
    if list(i.values())[0] == 'TMem%5FNO':
        config.BizMemberCode = i.get('value')
# while True:
#     # 获取当前时间
#     now = datetime.now()
#
#     # 检查当前时间是否为晚上七点（小时为19且分钟为0）
#     if now.hour == 19 and now.minute == 00:
#         print("It's 7 PM!")
#         break
#
#     # 等待0.1秒后再次检查
#     time.sleep(0.3)
#
driver.get(url=config.getInitialUrl(BizMemberCode=config.BizMemberCode))


def solve_recaptcha(tab):
    recaptchaSolver = RecaptchaSolver(tab)
    while True:
        try:
            recaptchaSolver.solveCaptcha()
            break
        except Exception as e:
            print(e)


time.sleep(2)
if driver.get_tab(title="인터파크 티켓"):
    print("Waiting")
    driver.get_tab(title="인터파크 티켓").wait.title_change("INTERPARK", timeout=10000)
    print("Waiting Finished")
    time.sleep(3)

while True:
    tab = driver.get_tab(title="INTERPARK")
    if tab:
        break

if tab is not None:
    tab.run_cdp_loaded('Runtime.evaluate',
                       expression="alert=function(x){console.log(x)}")  # override interpark js functions
    tab.run_cdp_loaded('Runtime.evaluate', expression="window.close=function(x){console.log(x)}")

    tab.ele(f'xpath://*[@id="LargeNextBtnImage"]').click()
    driver.wait.doc_loaded()
    tab.run_cdp_loaded('Runtime.evaluate', expression="javascript:fnNextStep('P')")
    if tab.ele("@title=reCAPTCHA", timeout=1):
        print("Solving recaptcha")
        solve_recaptcha(tab)
    while True:
        try:
            tab.ele(f'xpath:/html/body/form[1]/div/div[1]/div[1]/div[1]/div/select[1]', timeout=3).select.by_value(
                config.TIME)
            tab.ele(f'xpath:/html/body/form[1]/div/div[1]/div[1]/div[1]/div/select[2]', timeout=3).select.by_index(1)
            time.sleep(1.5)
            seat_iframe = tab.get_frame('#ifrmSeatDetail').html
            avail_seats = find_seat(seat_iframe)
            # avail_seats = filter_golden_seat(find_seat(seat_iframe))
            if len(avail_seats) > 0:
                break
        except Exception as e:
            print(e)
            pass
    random_seat = random.choice(avail_seats)
    print(random_seat)
    SID = random_seat.get('me')
    tab.ele(f'xpath://*[@id="{SID}"]').before().click()
    tab.ele(f'xpath://*[@id="NextStepImage"]').click()
    tab.ele(f'xpath://*[@id="PriceRow001"]/td[3]/select').select.by_value("1")
    tab.ele(f'xpath://*[@id="SmallNextBtnImage"]').click()
    fillPersonalInfo(tab)
    tab.ele(f'xpath://*[@id="SmallNextBtnImage"]').click()
    fillPaymentInfo(tab)
