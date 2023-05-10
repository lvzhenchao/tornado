import sys

print(sys.path)

# # 1) import 包名[.模块名 [as 别名]]
# import my_package.module1 as m1
# m1.display(333)
# import my_package.module1
# my_package.module1.display(222)
#
# # 2) from 包名 import 模块名 [as 别名]
# from my_package import module1
# module1.display(111)
#
# # 3) from 包名.模块名 import 成员名 [as 别名]
# from my_package.module1 import display
# display(444)

# 4) 使用__init__.py来导入,并且在里面添加相应的设置：目前导入不成功
import my_package
my_package.module1.display(555)

clangs = my_package.CLanguage()
clangs.display()