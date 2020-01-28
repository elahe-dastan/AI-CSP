from math import log10, floor


class Node:
    def __init__(self):
        self.value = 0
        self.adjacent_nodes = []

    def add_adjacent_node(self, adjacent_node):
        self.adjacent_nodes.append(adjacent_node)

    def value_satisfiable(self):
        if self.unique_satisfiable_value() is not None:
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

    def combinational_multiplication_of_domain_of_neighbours(self, node_domain):
        mul_values = node_domain[self.adjacent_nodes[0]]
        for i in range(1, len(self.adjacent_nodes)):
            new_mul_values = []
            for v in mul_values:
                for q in node_domain[self.adjacent_nodes[i]]:
                    new_mul_values.append(v * q)
            mul_values = new_mul_values
        return mul_values

    def combinational_summation_of_domain_of_neighbours(self, node_domain):
        sum_values = node_domain[self.adjacent_nodes[0]]
        for i in range(1, len(self.adjacent_nodes)):
            new_sum_values = []
            for v in sum_values:
                for q in node_domain[self.adjacent_nodes[i]]:
                    new_sum_values.append(v + q)
            sum_values = new_sum_values
        return sum_values

    def shorten_domain_most_significant_digit(self,node_domain, fc_domain):
        possible_value = set()
        for value in fc_domain:
            possible_value.add(self.most_significant_value(value))
        possible_value = list(possible_value)
        node_domain[self] = [v for v in node_domain[self] if v in possible_value]

    def shorten_domain_least_significant_digit(self, node_domain, fc_domain):
        possible_value = set()
        for value in fc_domain:
            possible_value.add(self.least_significant_value(value))
        possible_value = list(possible_value)
        node_domain[self] = [v for v in node_domain[self] if v in possible_value]

    def multiplication_of_neighbours_value(self):
        multiplication = 1
        for node in self.adjacent_nodes:
            if node.value == 0:
                return None
            multiplication = multiplication * node.value
        return multiplication

    def summation_of_neighbours_value(self):
        summation = 0
        for node in self.adjacent_nodes:
            if node.value == 0:
                return None
            summation += node.value
        return summation