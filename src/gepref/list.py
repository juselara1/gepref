from typing import List
from gepref.preprocessor import GenericPreprocessor
from gepref.step import AbstractStep

T = List[float]
class ListPreprocessor(GenericPreprocessor[T]): 
    """
    Default preprocessor for Python lists. This preprocessor is created mainly for testing purposes.

    :param steps: list of preprocessing steps
    :type steps: List[AbstractStep[List]]
    """
    ...

class IdentityStep(AbstractStep[T]):
    """
    A preprocessing step that implements the identity function.
    """

    def call(self, data: T) -> T:
        return data

class SquareStep(AbstractStep[List]):
    """
    A preprocessing step that implements the square function.
    """

    def call(self, data: T) -> T:
        return list(map(lambda i: i ** 2, data))
