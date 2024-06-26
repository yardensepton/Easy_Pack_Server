from abc import ABC, abstractmethod
from typing import List

from src.models.item import Item


class Filter(ABC):
    @abstractmethod
    def apply(self, items: List[Item]) -> List[Item]:
        pass
