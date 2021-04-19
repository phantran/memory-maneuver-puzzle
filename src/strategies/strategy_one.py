#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tran Phan
from src.modules.utils import timer
from src.strategies.strategy import Strategy


class StrategyOne(Strategy):
    """First strategy - use recursion"""

    @timer
    def execute(self, numbers_list: list) -> dict:
        """
        Args:
            numbers_list (list):
        """
        sum_meta, root_value = -1, -1
        try:
            sum_meta, _, root_value = self._analyze(numbers_list)
        except Exception:
            pass
        return {"sum_meta": sum_meta, "root_value": root_value}

    @classmethod
    def _analyze(cls, numbers_list: list) -> tuple:
        num_children = numbers_list[0]
        num_entries = numbers_list[1]
        remaining = numbers_list[2:]
        accumulated_sum = 0
        children_values = []

        for _ in range(num_children):
            # Part 1 - recurse and get the sum of entries of children
            child_sum_entries, remaining, child_node_value = cls._analyze(remaining)
            accumulated_sum += child_sum_entries
            # Part 2 - record children values of a node in children_values list
            children_values.append(child_node_value)

        node_sum_entries = sum(remaining[:num_entries])
        accumulated_sum += node_sum_entries

        # Part 2 - Calculating node value:
        # If a node has children then only consider children with a valid index
        # If a node has no children then its value is its entries sum
        node_value = cls._get_node_value(children_values,
                                         remaining[:num_entries]) if num_children != 0 else node_sum_entries

        return accumulated_sum, remaining[num_entries:], node_value

    @classmethod
    def _get_node_value(cls, children_values: list, parent_meta: list) -> int:
        # Get a node value by summing values of its children nodes
        # An entry in parent meta entries refers to the index of a child
        # Thus, skip an entry if its value is greater than the number of children or less than 1
        return sum(children_values[index - 1] for index in parent_meta if 1 <= index <= len(children_values))
