import sys
import hello
import dir

hello.say()

# 单独这样引入会报错
# 1、临时添加模块完整路径
# sys.path.append('E:\\python_code\\test\dir')
# dir.index()
print(type(dir))

print(sys.path)



