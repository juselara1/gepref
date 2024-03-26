from typing import TypeVar, Generic, List
from gepref.step import AbstractStep
from functools import reduce

T = TypeVar('T')
class GenericPreprocessor(Generic[T]):
    """
    Generic class that process an input data element through several preprocessing steps.

    :param steps: list of preprocessing steps
    :type steps: List[AbstractStep[T]]
    """
    def __init__(self, steps: List[AbstractStep[T]]) -> None:
        self.steps = steps

    def __call__(self, data: T) -> T:
        """
        Preprocess a data element.

        :param data: Input data.
        :type data: T
        :returns: Preprocessed data.
        :rtype: T
        """
        return self.call(data)

    def call(self, data: T) -> T:
        """
        Preprocess a data element.

        :param data: Input data.
        :type data: T
        :returns: Preprocessed data.
        :rtype: T
        """
        return reduce(lambda data, step: step(data), self.steps, data)
