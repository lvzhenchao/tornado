import config
import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),
            (r"/home", index.HomeHandler)
        ]

        # Python 2.x 中的写法
        # super(Application, self).__init__(handlers, **config.settings)

        # Python 3.x 中的写法
        super().__init__(handlers, **config.settings)