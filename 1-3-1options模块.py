import tornado.web # 基础web框架模块
import tornado.ioloop # 核心IO循环模块， 封装了Linux的epoll和BSD的kqueue,是框架高效的基础
import tornado.httpserver
from config import options

# 业务处理类，习惯加个handler
class IndexHandler(tornado.web.RequestHandler):

    # 处理get请求的，不能处理post请求
    def get(self, *args, **kwargs):
        # 对应http请求的方法
        # 给浏览器响应信息
        self.write("lzc is a good man 配置文件")


if __name__ == "__main__":

    print("list = ", options['list'])

    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])

    # 手动创建一个http服务器对象，这种更直观看到创建服务器了
    httpServer = tornado.httpserver.HTTPServer(app)
    # 单独给这个服务器绑定端口
    httpServer.bind(options['port'])
    httpServer.start(1)

    # IOLoop.current()：返回当前线程的IOLoop实例对象
    # IOLoop.start()：启动IOLoop实例对象的I/O循环，同时开启了监听
    tornado.ioloop.IOLoop.current().start()
