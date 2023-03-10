"""example from F.Lott, Dusty Phillips"""

from typing import Iterable, Iterator

class CapitalIterable(Iterable[str]):
    def __init__(self, string:str) -> None:
        self.string = string

    def __iter__(self) -> Iterator[str]:
        """ returns iterator"""
        return CapitalIterator(self.string)

class CapitalIterator(Iterator[str]):
    def __init__(self, string: str) -> None:
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self) -> str:
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index +=1
        return word


if __name__=="__main__":
    sentence = "hello world this is a test of iterator pattern"
    iteratble = CapitalIterable(sentence)

    for i in iteratble:
        print(i)


    iterator = iter(iteratble)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break
