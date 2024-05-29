#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : 
# @Time    : 2024/5/29 18:21
# @File    : seatFilter.py
# @annotation    :
import re

def find_seat(html_text):
    seats = []
    allseats = []
    keys = ["me", "SeatGrade", "Floor", "RowNo", "SeatNo", "Block"]
    pattern = re.compile(r"alt=\"\" onclick=\"javascript: SelectSeat(.*)'")
    matches = pattern.findall(html_text)
    for match in matches:
        match = str(match).strip("(").replace("'", '').split(',')
        match = [i.strip().replace('열', '') for i in match]
        mapped_dict = dict(zip(keys, match))
        try:
            if int(mapped_dict.get("RowNo")) == 7 and int(mapped_dict.get("SeatNo")) in [24, 25, 26, 27]:
                print("Remove: ", mapped_dict)
                continue
        except Exception as e:
            continue
        allseats.append(mapped_dict)
        if '1층' in mapped_dict.get('Floor'):
            seats.append(mapped_dict)
    if len(seats) > 0:
        return seats
    else:
        print(allseats)
        print("Couldn't find 1st floor seats")
        return allseats


def filter_golden_seat(seats):
    golden_seats = []
    for seat_dict in seats:
        try:
            if int(seat_dict.get('RowNo')) <= 9 and 2 <= int(seat_dict.get('SeatNo')) <= 24:
                golden_seats.append(seat_dict)
        except Exception as e:
            continue
    if len(golden_seats) > 0:
        return golden_seats
    else:
        print("Couldn't find golden seats")
        return seats