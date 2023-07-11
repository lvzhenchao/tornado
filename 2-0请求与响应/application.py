import config
import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),
            (r"/home", index.HomeHandler),
            (r"/sunck", index.SunckHandler, {'word1': "good", "word2": "nice"}),

            # json
            (r"/json1", index.Json1Handler),
            (r"/json2", index.Json2Handler),

            # header
            (r"/header", index.HeaderHandler),

            # 状态码
            (r"/status", index.StatusHandler),

            # 重定向
            (r"/redirect", index.RedirectHandler),

            # 错误处理
            # iserror?flag=2
            (r"/error", index.ErrorHandler),

            # 反向代理；bu能使用上面的元组路由；
            tornado.web.url(r'/kaige', index.KaigeHandler, {"word3": "lzc456","word4": "lzc789"}, name="kaigeGood"),

        ]

        # Python 2.x 中的写法
        # super(Application, self).__init__(handlers, **config.settings)

        # Python 3.x 中的写法,重写父类的初始化方法
        super().__init__(handlers, **config.settings)