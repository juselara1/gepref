from typing import TypeVar, Generic, List
from gepref.step import AbstractStep
from functools import reduce

T = TypeVar('T')
class GenericPreprocessor(Generic[T]):
    def __init__(self, steps: List[AbstractStep[T]]) -> None:
        self.steps = steps

    def __call__(self, data: T) -> T:
        return self.call(data)

    def call(self, data: T) -> T:
        return reduce(lambda data, step: step(data), self.steps, data)
