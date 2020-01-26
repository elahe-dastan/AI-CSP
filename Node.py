from math import log10, floor


class Node:
    def __init__(self):
        self.value = 0
        self.adjacent_nodes = []

    def add_adjacent_node(self, adjacent_node):
        self.adjacent_nodes.append(adjacent_node)

    def value_satisfiable(self):
        if self.unique_satisfiable_value() != 10:
            if self.value != self.unique_satisfiable_value():
                return False
        return True

    def unique_satisfiable_value(self):
        print("should never ever be here")

    def remove_intercalary_domain(self, node_domain):
        print("should never ever be here")
        
    def most_significant_value(self, value):
        return floor(value / (10 ** floor(log10(value))))

    def least_significant_value(self, value):
        return value % 10