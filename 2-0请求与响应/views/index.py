import json

import tornado.web
from tornado.web import RequestHandler

# 业务处理类，习惯加个handler
class IndexHandler(RequestHandler):

    # 处理get请求的，不能处理post请求
    def get(self, *args, **kwargs):
        # 对应http请求的方法
        # 给浏览器响应信息
        # self.write("lzc is a good man 呕呕呕")
        url = self.reverse_url("kaigeGood")
        # print(url)  返现代理跳转
        self.write("<a href='%s' > 去另一个界面 </a>"%(url))

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

        # 手动设置改变返回格式，改变响应头
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.set_header("lzc", "good man")
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

class HeaderHandler(RequestHandler):

    # 在http响应处理方法之前被调用，可以重写该方法来预先设置默认的headers；
    # 默认方法
    def set_default_headers(self):
        self.set_header("Content-Type", "text/html; charset=UTF-8")
        self.set_header("lzc", "1")
    def get (self, *args, **kwargs):
        self.set_header("lzc", "2")
        self.write("good nice")

    def post(self, *args, **kwargs):
        pass

class StatusHandler(RequestHandler):
    def get (self, *args, **kwargs):
        self.set_status(404, "没遭到") #必须是正常的code码，reason值才可以正常显示
        self.write("#########")

    def post(self, *args, **kwargs):
        pass

class RedirectHandler(RequestHandler):
    def get (self, *args, **kwargs):
        self.redirect("/")

class ErrorHandler(RequestHandler):

    # 用来处理send_error抛出的错误信息，并返回给浏览器错误界面
    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            code = 500
            self.write("服务器颞部错误")
        elif status_code == 404:
            code = 404
            self.write("资源不存在")
        else:
            code = 999
            self.write("不知道啥错误")

        self.set_status(code)

    def get (self, *args, **kwargs):
        flag = self.get_query_argument("flag")
        print(type(flag))
        if flag == "0":
            # send_error抛出错误状态码，默认为500，抛出后会调用write_error方法进行处理
            # 在send_error之后就不要在响应输出了
            self.send_error(500)

        self.write("You are Right")

class KaigeHandler(RequestHandler):

    def initialize(self, word3, word4):
        self.word3 = word3
        self.word4 = word4
    def get (self, *args, **kwargs):
        print(self.word3, self.word4)
        self.write("lzc is good man")

class LiuyifeiHandler(RequestHandler):
    def get (self,h1,h2,h3, *args, **kwargs):

        print(h1+"-"+h2+"-"+h3)
        self.write("lzc is good man")




