# -*- coding: utf8 -*-
import Exception as Exception
from django.http import HttpResponse
from django.shortcuts import render_to_response
from koubeijie.service.wechat_service import *


def hello(request):
    return HttpResponse("Hello World")


def wechat_login(request):
    try:
        # code参数检查
        code = request.GET.get('code')
        if not code:
            print "code is null"
            return render_to_response("login/wechat_error.html")

        # 通过code获取token、openid
        request_dict = get_access_token(code)
        if "errcode" in request_dict:
            print "get token,openid error"
            return render_to_response("login/wechat_error.html")
        access_token = request_dict.get("access_token")
        openid = request_dict.get("openid")

        # 拉取用户信息
        request_dict = get_user_info(access_token, openid)
        if "errcode" in request_dict:
            print "get userinfo error"
            return render_to_response("login/wechat_error.html")

        # 根据信息渲染模板
        return render_to_response("login/wechat.html", request_dict)
    except Exception as e:
        print e

def wx(request):
    return request.GET.get('echostr')