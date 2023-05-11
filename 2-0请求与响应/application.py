import config

import tornado.web

# 下面两种写法都可以
import views
# import views.index
# from views import index
# from views.index import IndexHandler
class Application(tornado.web.Application):
    def __int__(self):
        handlers = [
            # app = tornado.web.Application([
            # from views import index
            # (r"/", index.IndexHandler)

            # import views.index
            # (r"/", views.index.IndexHandler)

            # from views.index import IndexHandler
            # (r"/", IndexHandler)

            # import view
            (r"/", views.index.IndexHandler),
            (r"/home", views.index.HomeHandler)
        ]

        super(Application, self).__init__(handlers, **config.settings)