"""example from Eckel. B."""

class ApplicationFramework:
    def __init__(self):
        self.__templateMethod()

    def __templateMethod(self):
        for i in range(5):
            self.customize1()
            self.customize2()

class MyAPP(ApplicationFramework):
    def customize1(self):
        print("Nudge, nudge, wink. wink! ",)
    def customize2(self):
        print("Say no more, Say no more!")

MyApp()