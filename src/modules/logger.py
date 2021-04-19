import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)


def info(message: str):
    logging.info(message)


def exception(message: str):
    logging.exception(message)


def error(message: str):
    logging.error(message)
