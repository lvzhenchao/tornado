import tornado.web # 基础web框架模块
import tornado.ioloop # 核心IO循环模块， 封装了Linux的epoll和BSD的kqueue,是框架高效的基础

# 业务处理类，习惯加个handler
class IndexHandler(tornado.web.RequestHandler):

    # 处理get请求的，不能处理post请求
    def get(self, *args, **kwargs):
        # 对应http请求的方法
        # 给浏览器响应信息
        self.write("lzc is a good man 多进程")


if __name__ == "__main__":

    # 用这个类：tornado.web.Application，实例化一个应用对象
    # Application：是tornado web 框架的核心应用类，是与服务对应的接口
    # 里面保存了路由映射表
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    # 有一个listen方法来创建一个http服务器的实例，并绑定了监听端口
    # 注意：此时服务器并没有开启监听
    # 1、这是一种创建HTTPServer，并且同时绑定一个端口
    # app.listen(8888)

    # 2、手动创建一个http服务器对象，这种更直观看到创建服务器了
    httpServer = tornado.httpserver.HTTPServer(app)
    # 单独给这个服务器绑定端口
    # httpServer.listen(8888)
    httpServer.bind(8887)
    httpServer.start(5)

    # IOLoop.current()：返回当前线程的IOLoop实例对象
    # IOLoop.start()：启动IOLoop实例对象的I/O循环，同时开启了监听
    tornado.ioloop.IOLoop.current().start()