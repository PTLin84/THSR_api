from main import show_json
import requests
import json
import pandas as pd
import re
import datetime

URL = 'http://ptx.transportdata.tw/MOTC/v2/Rail/THSR/DailyTimetable/TrainDate/?TrainDate=2020-12-01&$format=json'

pd.set_option('display.max_rows', None)
pd.set_option('display.unicode.east_asian_width', True)


response_get = requests.get(URL)
data = json.loads(response_get.text)
show_json(data)
