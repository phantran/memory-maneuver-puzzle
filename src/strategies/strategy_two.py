from src.modules.utils import timer
from src.strategies.strategy import Strategy


class StrategyTwo(Strategy):
    """Second strategy - use stack"""

    @timer
    def execute(self, numbers_list: list) -> dict:
        """
        Args:
            numbers_list (list):
        """
        try:
            root_node = Node(numbers_list[0], numbers_list[1])
            nodes_stack = [root_node]
            sum_val = 0
            i = 2
            while nodes_stack:
                top_node = nodes_stack[-1]
                if top_node.children_left > 0:
                    child_node = Node(numbers_list[i], numbers_list[i + 1])
                    top_node.children_nodes.append(child_node)
                    i += 2
                    nodes_stack.append(child_node)
                    top_node.children_left -= 1

                elif top_node.num_entries > 0:
                    node_entries = numbers_list[i: i + top_node.num_entries]
                    sum_node_entries = sum(node_entries)
                    sum_val += sum_node_entries

                    # Part 2 - Calculating node value:
                    if top_node.num_children == 0:
                        top_node.value = sum_node_entries
                    else:
                        top_node.value = sum(top_node.children_nodes[i - 1].value for i in node_entries
                                             if 1 <= i <= top_node.num_children)
                    i += top_node.num_entries
                    nodes_stack.pop()

            return {"sum_meta": sum_val, "root_value": root_node.value}
        except Exception:
            return {"sum_meta": -1, "root_value": -1}


class Node:
    def __init__(self, num_children, num_entries):
        self.num_children = num_children
        self.children_left = num_children  # presents number of children left to be processed of a node
        self.num_entries = num_entries
        self.children_nodes = []  # contains references to children nodes of a node
        self.value = 0  # value of a node
