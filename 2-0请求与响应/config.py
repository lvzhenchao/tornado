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
    "autoreload": True, # 只需要自动重启，就使用这个参数
    # "debug": True,
    # 设置tornado是否工作在调试模式下，默认为false即工作在生产下；
    # True：自动重启，监控源码是否有变动，判断是否重启服务器，减少手动重启，提高开发效率；单独使用autoreload = True
    # True：取消缓存编译的模版； 可以使用这个单独的参数compiled_template_cache = False/True单独设置
    # True：取消缓存静态文件的hash值； 单独设置 static_hash_cache = False
    # True：提供追踪信息；单独通过serve_traceback=True;一般不使用
}