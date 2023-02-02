"""Purpose:
1. Enhancing the response of a component as it sends data to a second component.
2. Supporting multiple optional behaviours. This can serve as an alternative to multiple inheritance.
Core Interface is preserved and decorator maintain a reference to the core via composition.
It is possible to decorate already decorated objects. Functions, methods and classes can be decorated."""

import logging
import time
import typing
from typing import Callable, Any
from functools import wraps


class NamedLogger:
    def __init__(self, logger_name:str) -> None:
        self.logger = logging.getLogger(logger_name)

    def __call__(self, function: Callable[..., Any]) -> Callable[..., Any]:
        """ The call function allows classes, where instances behave like a function"""
        @wraps(function)
        def wrapped_function(*args: Any, **kwags: Any) -> Any:
            start = time.perf_counter()
            try:
                result = function(*args,**kwags)
                mus = (time.perf_counter()-start)*1_000_000
                self.logger.info(f"{function.__name__}, {mus:.1f}mus")
                return result

            except Execution as ex:
                mus = (time.perf_counter()-start)*1_000_000
                self.logger.error(f"{function.__name__}, {mus:.1f}mus")
                raise

        return wrapped_function

if __name__=="__main__":
    @NamedLogger("log4")
    def test4(median: float, sample: float) -> float:
        return abs(sample-median)
    result = test4(5,6)
    print(result)

