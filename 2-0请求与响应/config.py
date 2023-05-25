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
    "debug": True,
}