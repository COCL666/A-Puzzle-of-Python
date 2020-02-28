#!/usr/local/bin/python3
import json
import requests
import sys

def send_msg(url, remiders, msg):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    data = {
        "msgtype": "text",  #text类型,link类型,markdown类型
        "at": {
            "atMobiles": remiders,
            "isAtAll": False,
        },
        "text": {
            "content": msg,
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == '__main__':
    msg = sys.argv[1]
    remiders = []
    url = 'https://oapi.dingtalk.com/robot/send?access_token=a91de8c0045b565d230a0fc18fda55be3362b35d109cbeda9f4e24de2acdedc1'
    print(send_msg(url, remiders, msg))

