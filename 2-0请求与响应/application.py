import config
import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),
            (r"/home", index.HomeHandler),
            (r"/sunck", index.SunckHandler, {'word1': "good", "word2": "nice"}),

            (r"/json1", index.Json1Handler),
            (r"/json2", index.Json2Handler),

            (r"/header", index.HeaderHandler),
        ]

        # Python 2.x 中的写法
        # super(Application, self).__init__(handlers, **config.settings)

        # Python 3.x 中的写法
        super().__init__(handlers, **config.settings)