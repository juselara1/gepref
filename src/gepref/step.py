from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class AbstractStep(ABC, Generic[T]):

    def __call__(self, data: T) -> T:
        return self.call(data)

    @abstractmethod
    def call(self, data: T) -> T:
        ...
