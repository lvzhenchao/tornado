import config
import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # app = tornado.web.Application([
            # from views import index
            # (r"/", index.IndexHandler)

            # import views.index
            # (r"/", views.index.IndexHandler)

            # from views.index import IndexHandler
            # (r"/", IndexHandler)

            # import view
            (r"/", index.IndexHandler),
            (r"/home", index.HomeHandler)
        ]

        super(Application, self).__init__(handlers, **config.settings)