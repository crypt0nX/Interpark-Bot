# Interpark-Bot

## Description

This is a simple example of a ticket-sniping program for Interpark Global, using DrissionPage. Please note that although it can successfully complete the task, it's likely not directly usable without some coding background, as the seating information for each venue is different and the process for each show may vary. This code is just an example. 

In config.py, you need to fill in two key variables based on the information of the different performances: GOODS_ID and TIME. Both variables can be found on the performance page. For example, using https://www.globalinterpark.com/en/product/24007162, GOODS_ID is the last set of numbers in the URL, 24007162, and TIME is the date of the performance, formatted as YYYYMMDD.

Please note that you will still need to modify two functions in utils.seat_filter to filter specific venue seats. This will require you to study the code yourself. Good luck!

### 声明

This code is for learning purposes only. Please delete it within 24 hours after downloading.