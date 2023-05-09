import tornado.web
from tornado.web import RequestHandler

# 业务处理类，习惯加个handler
class IndexHandler(RequestHandler):

    # 处理get请求的，不能处理post请求
    def get(self, *args, **kwargs):
        # 对应http请求的方法
        # 给浏览器响应信息
        self.write("lzc is a good man 呕呕呕")