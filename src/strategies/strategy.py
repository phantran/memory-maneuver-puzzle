from typing import List
from abc import ABC, abstractmethod

Input_Data = List[int]


class Strategy(ABC):
    """ Base class of puzzle solving strategies, subclass this base class to implement a new strategy
    """

    @abstractmethod
    def execute(self, numbers_list: Input_Data):
        """
        Args:
            numbers_list (Input_Data):
        """
        pass
