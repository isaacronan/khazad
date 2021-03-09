from abc import ABC, abstractmethod

class Value(ABC):
    @abstractmethod
    def resolve():
        pass