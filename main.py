# reference code from Github:
# https://github.com/music1353/pyHowFun/blob/master/LESSON4%20%E7%88%AC%E8%9F%B2%E5%AF%A6%E6%88%B0%20-%20%E9%AB%98%E9%90%B5%E6%99%82%E5%88%BB.ipynb
# this program uses "requests.post" to upload data for online form submission and gets the response data

URL = 'https://www.thsrc.com.tw/TimeTable/Search'


def show_json(seq, n=0):
    if type(seq) is dict:
        for key, value in seq.items():
            if type(value) in [list, tuple]:
                for child in value:
                    if type(child) is dict:
                        print(f'{n * "    "}{key}:')
                        show_json(child, n+1)
                    else:
                        print(f'{n * "    "}{key}: ', end='')
                        print(child)
            elif type(value) is dict:
                print(f'{n*"    "}{key}:')
                show_json(value, n+1)
            elif type(value) in [str, int]:
                print(f'{n*"    "}{key}: {value}')

# 1 dict {key: [list, tuple]}
    # 1-1 print(key)
    # 1-2 check list/tuple
        # 1-2-1 print(list, tuple)
        # 1-2-2 list/tuple contains dict
# 2 dict {key: [dict]}
    # 2-1 print(key)
    # 2-2 print(dict)
# 3 dict {key: value}
    # 3-1 print(key + value)


# a = [['this', 'is'], ['a', ['dog', 'cat', ['mouse']], 'ha'], 'wow']


import requests
from bs4 import BeautifulSoup
import json

form_data = {
    'SearchType': 'S',
    'Lang': 'TW',
    'StartStation': 'TaiPei',
    'EndStation': 'ZuoYing',
    'OutWardSearchDate': '2020/12/24',
    'OutWardSearchTime': '18:30',
    'ReturnSearchDate': '2020/12/4',
    'ReturnSearchTime': '12:00',
    'DiscountType': ''
}

response_post = requests.post(URL, data=form_data)
data = json.loads(response_post.text)
trainItem = data['data']['DepartureTable']['TrainItem']

