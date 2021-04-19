from src.input.source import DataSource
from src.modules import logger


class CmdInput(DataSource):

    def __init__(self, input_data: list):
        """
        Args:
            input_data (list):
        """
        try:
            super().__init__(self._parse_input(input_data))
        except ValueError as e:
            logger.error("EXIT - Please make sure cmd arguments for numbers lists contain only integer values")
            raise e
        except Exception as e:
            logger.exception("EXIT - Error while getting data from the cmd arguments")
            raise e

    @staticmethod
    def _parse_input(input_data: list) -> list:
        """
        Args:
            input_data (list):
        """
        res = []
        try:
            for lst in input_data:
                res.append(list(map(int, lst)))
        except Exception as e:
            raise e

        return res
