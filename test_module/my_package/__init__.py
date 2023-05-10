'''
http://c.biancheng.net/
创建第一个 Python 包
'''
print('http://c.biancheng.net/python/')

# 第 1 种方式用于导入当前包（模块）中的指定模块：from . import 模块名
from . import module1

# 第 2 种方式表示从指定模块中导入所有成员，采用这种导入方式，在其他程序中使用该模块的成员时，只要使用包名作为前缀即可
# 从.模块名 导入所有成员到包中
from .module2 import *