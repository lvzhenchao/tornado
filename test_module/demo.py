'''
demo 模块中包含以下内容：
name 字符串变量：初始值为“Python教程”
add  字符串变量：初始值为“http://c.biancheng.net/python”
say() 函数
CLanguage类：包含 name 和 add 属性和 say() 方法。
'''
name = "Python教程"
add = "http://c.biancheng.net/python"
print(name,add)
def say():
    print("人生苦短，我学Python！")
class CLanguage:
    def __init__(self,name,add):
        self.name = name
        self.add = add
    def say(self):
        print(self.name,self.add)

if __name__ == '__main__':
    say()
    clangs = CLanguage("C语言中文网","http://c.biancheng.net")
    clangs.say()