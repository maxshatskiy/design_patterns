class OnlyOne:
    """One way to implement Singleton"""
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return 'self'+self.val
    instance = None

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, item):
        return getattr(self.instance, name)


class OneOnly:
    """Alternative implementation of singleton"""
    _singleton = None
    def __new__(cls, *args,**kwargs):
        """ called when object is created. while __init__ to initialize the object"""
        if not cls._singleton: # create new object only if there is no exist
            cls._singleton=super().__new__(cls, *args,**kwargs)
        return cls._singleton




if __name__=="__main__":

    x = OnlyOne('sausage')
    print(x)
    print(OnlyOne.instance)
    print(x.instance)
    print(id(OnlyOne.instance))
    print(id(x.instance))
    y = OnlyOne('eggs')
    print(y)
    print(OnlyOne.instance)
    z = OnlyOne('spam')
    print(z)
    print(OnlyOne.instance)
    print('x')
    print('y')
    print('z')

    o1 = OneOnly()
    o2 = OneOnly()
    print(id(o1) == id(o2))
    print(o1)
    print(o1._singleton)
    print(o2)