"""from Eckel B."""
class A:
    def __init__(self,x): pass

class B:
    def __init__(self,x): pass

class C:
    def __init__(self,x): pass

class Facade:
    @staticmethod
    def makeA(x): return A(x)

    @staticmethod
    def makeB(x): return B(x)

    @staticmethod
    def makeC(x): return C(x)

a = Facade.makeA(1)
b = Facade.makeB(1)
c = Facade.makeC(1.0)