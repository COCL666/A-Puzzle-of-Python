#!/usr/local/bin/python3
import json
import requests


def send_msg(url, remiders):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    data = {
        "msgtype": "markdown",  # text类型,link类型,markdown类型
        "at": {
            "atMobiles": remiders,
            "isAtAll": False,
        },
        "markdown": {
            "title": "女神 ",
            "text": "#### 石原里美 \n" +
                    "> 人家也不是二次元！！！\n\n" +
                    "> ![screenshot](https://dss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1515896429,1098150742&fm=26&gp=0.jpg)\n" +
                    "> ###### 出自钟力。。。 \n"
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text


if __name__ == '__main__':
    remiders = ["156*****005", "187*****148"]
    url = 'https://oapi.dingtalk.com/robot/send?access_token=a91de8c0045b565d230a0fc18fda55be3362b35d109cbeda9f4e24de2acdedc1'
    print(send_msg(url, remiders))
