from typing import List
from gepref.preprocessor import GenericPreprocessor
from gepref.step import AbstractStep

T = List[float]
class ListPreprocessor(GenericPreprocessor[T]): ...

class IdentityStep(AbstractStep[T]):
    def call(self, data: T) -> T:
        return data

class SquareStep(AbstractStep[List]):
    def call(self, data: T) -> T:
        return list(map(lambda i: i ** 2, data))
