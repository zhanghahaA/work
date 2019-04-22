class father:
    def myfn(self):
        print('调用父类方法')
class child(father):
    def myfn(self):
        print('调用子类方法')

s=child()
s.myfn()
super(child,s).myfn()