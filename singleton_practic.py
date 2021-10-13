class Onlyfirst:
    class __Onlyfirst:
        def __init__(self):
            self.val = None
        def __str__(self):
            return self.val
    instance = None
    def __new__(cls):
        if not Onlyfirst.instance:
            Onlyfirst.instance = Onlyfirst.__Onlyfirst()
        return Onlyfirst.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)
x = Onlyfirst()
x.val = 'Автомобиль'
print(x)
y = Onlyfirst()
y.val = 'Самолет'
print(y)
z = Onlyfirst()
z.val = 'Лодка'
print(z)
print(x)
print(y)
