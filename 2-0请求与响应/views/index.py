import json

import tornado.web
from tornado.web import RequestHandler

# 业务处理类，习惯加个handler
class IndexHandler(RequestHandler):

    # 处理get请求的，不能处理post请求
    def get(self, *args, **kwargs):
        # 对应http请求的方法
        # 给浏览器响应信息
        self.write("lzc is a good man 呕呕呕")

class HomeHandler(RequestHandler):

    # 处理get请求的，不能处理post请求
    def get(self, *args, **kwargs):
        # 对应http请求的方法
        # 给浏览器响应信息
        self.write("home is ok")

class SunckHandler(RequestHandler):
    #该方法会在HTTP方法之前调用
    def initialize(self, word1, word2):
        # 接收参数
        self.word1 = word1
        self.word2 = word2

    def get(self, *args, **kwargs):
        # 对应http请求的方法
        # 给浏览器响应信息
        print(self.word1, self.word2)
        self.write("lzc is a good man")

class Json1Handler(RequestHandler):
    def get (self, *args, **kwargs):
        per = {
            "name": "sunk",
            "age": 18,
            "height": 178,
            "weight": 70
        }

        # 将字典转换成json字符串
        # 浏览器返回信息：Content-Type:text/html; charset=UTF-8
        jsonStr = json.dumps(per)
        self.write(jsonStr)

class Json2Handler(RequestHandler):
    def get (self, *args, **kwargs):
        per = {
            "name": "sunk",
            "age": 18,
            "height": 178,
            "weight": 70
        }

        # write方法返回的直接是字典，
        # 浏览器返回信息显示：Content-Type:application/json; charset=UTF-8
        self.write(per)
