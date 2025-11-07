from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def price(self) -> float:
        pass
