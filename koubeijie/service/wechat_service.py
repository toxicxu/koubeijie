# -*- coding: utf8 -*-
import ConfigParser
import json
import requests
from collections import OrderedDict


# 根据code获取access_token
def get_access_token(code):
    config = ConfigParser.ConfigParser()
    config.read("koubeijie/config.ini")

    payload = OrderedDict()
    payload["appid"] = config.get("wechat", "appid")
    payload["secret"] = config.get("wechat", "secret")
    payload["code"] = code
    payload["grant_type"] = "authorization_code"

    ret = requests.get("https://api.weixin.qq.com/sns/oauth2/access_token", params=payload)
    return json.loads(ret.text.encode("raw_unicode_escape"))


# 拉取用户信息
def get_user_info(access_token, openid):
    payload = OrderedDict()
    payload["access_token"] = access_token
    payload["openid"] = openid
    payload["lang"] = "zh_CN"
    ret = requests.get("https://api.weixin.qq.com/sns/userinfo", params=payload)
    result_dict = json.loads(ret.text.encode("raw_unicode_escape"))

    if result_dict["sex"] == 1:
        result_dict["sex"] = "男"
    elif result_dict["sex"] == 2:
        result_dict["sex"] = "女"
    else:
        result_dict["sex"] = "未知"
    return result_dict

