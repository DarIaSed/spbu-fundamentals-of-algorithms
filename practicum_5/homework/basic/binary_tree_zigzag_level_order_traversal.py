from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import os
from collections import deque

import yaml


@dataclass
class Node:
    key: Any
    data: Any = None
    left: Node = None
    right: Node = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    def empty(self) -> bool:
        return self.root is None

    def zigzag_level_order_traversal(self) -> list[Any]:
        if self.empty():
            return []

        result = []
        queue = deque([self.root])
        zigzag = True

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.key)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            if zigzag:
                result.append(level_nodes)
            else:
                result.append(level_nodes[::-1])

            zigzag = not zigzag
        return result


def build_tree(list_view: list[Any]) -> BinaryTree:
    bt = BinaryTree()

    nodes = []

    for item in list_view:
        cur_node = Node(item)
        if not (cur_node.key is None):
            nodes.append(cur_node)
        for i, node in enumerate(nodes):
            if 2 * i + 1 < len(nodes):
                node.left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                node.right = nodes[2 * i + 2]
        bt.root = nodes[0]
    return bt


if __name__ == "__main__":

    with open("binary_tree_zigzag_level_order_traversal_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = build_tree(c["input"])
        zz_traversal = bt.zigzag_level_order_traversal()
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")
