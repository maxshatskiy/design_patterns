"""Usefull: for state monitoring and event handling situations.
This patter allows a given object to be monitored by an unknown and dynamic group of observer objects.
The observable core object needs to implement an interface.
If value of observable object changes it announces that there has been a change of state.

USAGE:
1. GUI
2. Saving intermediate states of objects.

From Aaron Maxwell:
"Observable object knows how to detect some kind of even: customer making a new purchase, subscription to an email list,
detect when usage exceeds 75%. Observable = publisher, which watches for events. Observers=subsribers, who ask that
publisher to notify them when the event happens."

"""
class Publisher:

    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print(f'Failed to add: {observer}')

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print(f'Failed to remove: {observer}')

    def notify(self):
        [o.notify(self) for o in self.observers] # this self is a publisher

class DefaultFormatter(Publisher):

    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return f"{type(self).__name__}: '{self.name}' has data = {self._data}"

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print(f'Error: {e}')
        else:
            self.notify() # run notify function in all observers attached to DefaultFormatter

class HexFormatterObs:
    def notify(self, publisher):
        value = hex(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now hex data = {value}")

class BinaryFormatterObs:
    def notify(self, publisher):
        value = bin(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now hex data = {value}")

def main():
    df = DefaultFormatter('test1')
    print(df)
    hf = HexFormatterObs()
    df.add(hf) # add observer to observable
    print('Observers {}'.format(df.observers))
    df.data = 3
    print(df)

    print()
    bf = BinaryFormatterObs()
    df.add(bf)
    df.data = 21
    print(df)

    print()
    df.remove(hf)
    df.add(bf)

    df.data = "hello"

    print()
    df.data = 15.8
    print(df)

if __name__=="__main__":
    main()