from typing import List
from abc import ABC, abstractmethod

Input_Data = List[List]


class DataSource(ABC):
    """ Base class of input data sources, subclass this base class to implement a new data source
    """

    def __init__(self, input_data: Input_Data):
        """
        Args:
            input_data (Input_Data):
        """
        self._numbers_lists = input_data

    @property
    def numbers_lists(self):
        return self._numbers_lists

    @staticmethod
    @abstractmethod
    def _parse_input(input_data) -> list:
        """
        Args:
            input_data:
        """
        return []
