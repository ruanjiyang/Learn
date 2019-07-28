class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print('class A')
    def add(self):
        return self.a+self.b

class B:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print('class B')
    def add(self):
        return self.a*2+self.b*2

class C(B,A):
    def __init__(self,a,b):
        super().__init__(a,b)
    def add(self):
        return super().add()

c=C(1,2)
print(c.add())

    
