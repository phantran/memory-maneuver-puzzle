#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tran Phan
from src.input.cmd import CmdInput
from src.input.file import FileInput
from src.modules import logger
from src.modules.arguments import get_console_arguments
from src.modules.utils import pretty_args
from src.solver import solve
from src.strategies.strategy_one import StrategyOne
from src.strategies.strategy_two import StrategyTwo


def process_args(args):
    strategy = None
    if args.chosen_strategy == 1:
        strategy = StrategyOne()

    if args.chosen_strategy == 2:
        strategy = StrategyTwo()

    if strategy is None:
        logger.info(f"EXIT - Chosen strategy is not supported")
        exit(1)

    data_source = None
    try:
        if args.input_mode == "cmd":
            if not args.numbers_lists:
                logger.info(f"EXIT - Please specify input data with the argument --l for the cmd input mode")
                exit(1)
            data_source = CmdInput(args.numbers_lists)
        elif args.input_mode == "file":
            data_source = FileInput(args.file_path)

        if data_source is None:
            logger.error("Exit - Cannot get input data")
            exit(1)

    except Exception:
        exit(1)

    return strategy, data_source


if __name__ == "__main__":
    logger.info("START")
    arguments = get_console_arguments()
    logger.info(pretty_args(arguments.__dict__))
    processed_args = process_args(arguments)  # Process console arguments
    solve(*processed_args)  # Solve puzzle
    logger.info("DONE")
