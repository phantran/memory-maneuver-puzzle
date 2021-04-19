from src.input.source import DataSource
from src.modules import logger


class FileInput(DataSource):

    def __init__(self, file_path: str):
        """
        Args:
            file_path (str):
        """
        try:
            input_data = self._parse_input(file_path)
            super().__init__(input_data)
        except ValueError as e:
            logger.error("EXIT - Please make sure the input file contains only integer values")
            raise e
        except FileNotFoundError as e:
            logger.error("EXIT - Please make sure path of the input file is correct")
            raise e
        except Exception as e:
            logger.exception("EXIT - Error while getting data from the input file")
            raise e

    @staticmethod
    def _parse_input(file_path: str) -> list:
        """
        Args:
            file_path (str):
        """

        # Could be improved with generator for big input file
        # Keep it simple in this solution
        res = []
        try:
            with open(file_path, 'r') as lines:
                for line in lines:
                    res.append(list(map(int, line.split())))
        except Exception as e:
            raise e

        return res
