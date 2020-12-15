from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import base64
from requests import request
from pprint import pprint
import json
from main import show_json

URL = 'http://ptx.transportdata.tw/MOTC/v2/Rail/THSR/DailyTimetable/TrainDate/?TrainDate=2020:12:24&$top=30&$format=JSON'

app_id = 'c4fc794ed9624955a1e5d0f133606c43'
app_key = 'A429yj6gzCL-S4QXRqhzu031EnE'

class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple())) # current time in format 'Sun, 13 Dec 2020 12:24:51 GMT'
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username="' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature="' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept - Encoding': 'gzip'
        }


if __name__ == '__main__':
    a = Auth(app_id, app_key)
    response = request('get', URL, headers= a.get_auth_header())
    # 'https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/Taipei?$top=30&$format=JSON'
    print(response.content)
    print(repr(response))
