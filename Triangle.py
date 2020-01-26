from math import log10, floor
from Node import Node


class Triangle(Node):
    def unique_satisfiable_value(self):
        multiplication = 1
        for node in self.adjacent_nodes:
            if node.value == 0:
                return 10
            multiplication = multiplication * node.value
        most_significant_digit = floor(multiplication / (10**floor(log10(multiplication))))
        return most_significant_digit

    def remove_intercalary_domain(self, node_domain):
        mul_values = node_domain[self.adjacent_nodes[0]]
        for i in range(1, len(self.adjacent_nodes)):
            new_mul_values = []
            for v in mul_values:
                for q in node_domain[self.adjacent_nodes[i]]:
                    new_mul_values.append(v * q)
            mul_values = new_mul_values
        possible_value = set()
        for value in mul_values:
            possible_value.add(self.most_significant_value(value))

        possible_value = list(possible_value)
        node_domain[self] = [v for v in node_domain[self] if v in possible_value]

