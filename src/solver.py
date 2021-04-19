#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tran Phan
from src.input.source import DataSource
from src.strategies.strategy import Strategy
from src.modules import logger


def solve(strategy: Strategy, data_source: DataSource):
    filtered_lists = filter(lambda x: not len(x) == 0, data_source.numbers_lists)  # Skip input as empty numbers lists
    res = list(map(lambda x: strategy.execute(x), filtered_lists))  # Solve the puzzle

    # Pretty print results
    logger.info("")
    logger.info(f"========================= Result =========================")
    for i in range(len(res)):
        logger.info(f"Input {i + 1}")
        item = res[i][0]
        elapsed_time = res[i][1]
        if item["sum_meta"] == -1:
            logger.error("Skipped - Input data might be an invalid tree")
        else:
            logger.info(f"Elapsed time {elapsed_time:.4f} ms")
            logger.info(f"Part 1 - Sum metadata entries: {item['sum_meta']}")
            logger.info(f"Part 2 - Root node value: {item['root_value']}")
        logger.info("")
