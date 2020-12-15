# this program uses "requests.get" to access THSR's official API

import main  # main.py is imported here for the use of function "show_json"
import requests
import pandas

URL = 'https://ptx.transportdata.tw/MOTC/v2/Rail/THSR/DailyTimetable/OD/0990/to/1070/2020-12-10?$top=30&$format=JSON'

my_headers = {
    'Property': 'User-Agent',
    'Value': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

response = requests.get(URL, params=None, headers = my_headers)
repr(response)



