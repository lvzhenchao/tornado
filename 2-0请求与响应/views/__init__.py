# from index import IndexHandler
from tornado.web import RequestHandler
class IndexHandler(RequestHandler):

    # 处理get请求的，不能处理post请求
    def get(self, *args, **kwargs):
        # 对应http请求的方法
        # 给浏览器响应信息
        self.write("lzc is a good man 哈哈哈")