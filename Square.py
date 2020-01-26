from Node import Node


class Square(Node):
    def unique_satisfiable_value(self):
        multiplication = 1
        for node in self.adjacent_nodes:
            if node.value == 0:
                return 10
            multiplication = multiplication * node.value
        least_significant_digit = multiplication % 10
        if least_significant_digit == 0:
            return 10
        return least_significant_digit

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
            possible_value.add(self.least_significant_value(value))

        possible_value = list(possible_value)
        node_domain[self] = [v for v in node_domain[self] if v in possible_value]

    def remove_not_multiples_from_domain(self, adjacent_node_assignement):
        admissible_values = []
        for i in range(1, 10):
            admissible_values.append(adjacent_node_assignement * i)
        for value in self.domain_values:
            if value not in admissible_values:
                self.domain_values.remove(value)
