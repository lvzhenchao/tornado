import tornado.web # 基础web框架模块
import tornado.ioloop # 核心IO循环模块， 封装了Linux的epoll和BSD的kqueue,是框架高效的基础
import tornado.httpserver
from config import options
import views

if __name__ == "__main__":

    app = tornado.web.Application([
    #     # from views import index
    #     # (r"/", index.IndexHandler)
    #
    #     # import views.index
    #     # (r"/", views.index.IndexHandler)
    #
    #     # from views.index import IndexHandler
    #     # (r"/", IndexHandler)
    #
    #     # import view
        (r"/", views.index.IndexHandler)
    ])

    # 手动创建一个http服务器对象，这种更直观看到创建服务器了
    httpServer = tornado.httpserver.HTTPServer(app)
    # 单独给这个服务器绑定端口
    httpServer.bind(options['port'])
    httpServer.start(1)

    # IOLoop.current()：返回当前线程的IOLoop实例对象
    # IOLoop.start()：启动IOLoop实例对象的I/O循环，同时开启了监听
    tornado.ioloop.IOLoop.current().start()
