class MyClass:
    i = 1234

    def __init__(self):
        self.data=[]

    def __init__(self, data):
        self.data=data

    def f(self):
        return 'Hello, OOp!'


print(MyClass.i, MyClass.f)
#x=MyClass() #constructor
x=MyClass([1,2,3,4,5])
print(x.f(), x.f)
print(x.data)
y=MyClass(['a', 'b','c','d','e','f'])  #constructor
print(y.data, y.i)
