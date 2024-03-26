from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')
class AbstractStep(ABC, Generic[T]):
    """
    Interface that defines the behavior of a generic preprocessing step for a given data type `T`.
    It requires to implement the `call` method.
    """

    def __call__(self, data: T) -> T:
        """
        Preprocess an input data element.

        :param data: Input data element.
        :type data: T
        :returns: Preprocessed data.
        :rtype: T
        """
        return self.call(data)

    @abstractmethod
    def call(self, data: T) -> T:
        ...
