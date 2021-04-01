import re
import collections
from typing import Dict


def parse_line(line):
    line_parts = line.split("contain")
    parent_bag = line_parts[0][:-6]
    child_bags = []
    if not line.endswith("no other bags."):
        child_bag_parts = line_parts[1].split(",")
        for child_bag_part in child_bag_parts:
            count, child_bag = re.match(r".*(\d+) ([\w\s]+) bag", child_bag_part).groups()
            child_bags.append((child_bag, int(count)))
    return parent_bag, child_bags


def parse_input(lines):
    parsed_lines = [parse_line(line) for line in lines]
    return Graph(parsed_lines)


def solve1(input):
    graph = parse_input(input.splitlines())
    graph.reverse()
    return len(graph.bfs_linked_nodes("shiny gold")) - 1


def solve2(input):
    graph = parse_input(input.splitlines())
    return graph.bfs_subtree_weight("shiny gold") - 1


class Graph:
    nodes: Dict[str, Dict[str, int]]  # node -> outgoing edges

    def __init__(self, edges_list):
        self.nodes = {parent: {child: weight for child, weight in edges} for parent, edges in edges_list}

    def reverse(self):
        reversed_nodes = {}
        for target_node, edges in self.nodes.items():
            for source_node, weight in edges.items():
                if source_node not in reversed_nodes.keys():
                    reversed_nodes[source_node] = {}
                if target_node not in reversed_nodes.keys():
                    reversed_nodes[target_node] = {}
                reversed_nodes[source_node][target_node] = weight
        self.nodes = reversed_nodes

    def bfs_linked_nodes(self, start_node):
        nodes_deque = collections.deque([start_node])
        result = set()
        while len(nodes_deque) > 0:
            node = nodes_deque.popleft()
            for linked_node in self.nodes[node].keys():
                nodes_deque.append(linked_node)
            result.add(node)
        return result

    def bfs_subtree_weight(self, start_node):
        nodes_deque = collections.deque([(start_node, 1)])
        result = 0
        while len(nodes_deque) > 0:
            node, node_weight = nodes_deque.popleft()
            for linked_node, edge_weight in self.nodes[node].items():
                nodes_deque.append((linked_node, node_weight*edge_weight))
            result += node_weight
        return result
