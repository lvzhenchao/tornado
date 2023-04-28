import tornado.web # 基础web框架模块
import tornado.ioloop # 核心IO循环模块， 封装了Linux的epoll和BSD的kqueue,是框架高效的基础
import tornado.httpserver
from tornado import options

# 1、自定义定义两个参数
tornado.options.define("port", default = 8899, type = int)
tornado.options.define("list", default = [123,456], type = str, multiple=True)



# 业务处理类，习惯加个handler
class IndexHandler(tornado.web.RequestHandler):

    # 处理get请求的，不能处理post请求
    def get(self, *args, **kwargs):
        # 对应http请求的方法
        # 给浏览器响应信息
        self.write("lzc is a good man 多进程")


if __name__ == "__main__":

    # 2、转换命令行参数，并保存到tornado.options.options
    tornado.options.parse_command_line() #在解析和使用选项之前，您需要“define”选项
    print("list = ", tornado.options.options.list)
    print("port = ", tornado.options.options.port)

    # 3、获取一个配置文件的参数设置; 在解析和使用选项之前，您需要“define”选项
    tornado.options.parse_config_file("./config")
    print("list = ", tornado.options.options.list)
    print("port = ", tornado.options.options.port)

    app = tornado.web.Application([
        (r"/", IndexHandler)
    ])


    # 手动创建一个http服务器对象，这种更直观看到创建服务器了
    httpServer = tornado.httpserver.HTTPServer(app)
    # 单独给这个服务器绑定端口
    httpServer.bind(tornado.options.options.port)
    httpServer.start(1)

    # IOLoop.current()：返回当前线程的IOLoop实例对象
    # IOLoop.start()：启动IOLoop实例对象的I/O循环，同时开启了监听
    tornado.ioloop.IOLoop.current().start()

# options 基础方法和属性
## define()方法：定义变量
## parse_command_line()方法：解析命令行的参数，并保存到options
## parse_config_file(path)方法：从配置文件导入参数