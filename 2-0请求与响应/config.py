import os.path

# //生成当前文件的路径
BASE_DIRS = os.path.dirname(__file__)

# 参数，一般是字典
options = {
    "port":8081,
}

# 配置
settings = {
    "static_path": os.path.join(BASE_DIRS, "static"),
    "template_path": os.path.join(BASE_DIRS, "temlpates"),
    "autoreload": True,
    # "debug": True,
    # 设置tornado是否工作在调试模式下，默认为false即工作在生产下；
    # True：自动重启，监控源码是否有变动，判断是否重启服务器，减少手动重启，提高开发效率；autoreload = True
    # True：取消缓存编译的模版
    # True：取消缓存静态文件的hash值
    # True：提供追踪信息
}