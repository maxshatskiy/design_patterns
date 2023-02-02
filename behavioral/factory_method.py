"""Objects are created by a factory method.
Usage:
1. when we want to provide users with a way to extend its components.
2. when we want to save system resources by reusing exiting objects instead of rebuilidng them."""

from __future__ improt annotations
from abc import ABC, abstractmethod

class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def do_something(selfself):

        product = self.factory_method()

        result="test"

        return result