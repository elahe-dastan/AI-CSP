from Node import Node


class Pentagon(Node):
    def unique_satisfiable_value(self):
        summation = 0
        for node in self.adjacent_nodes:
            if node.value == 0:
                return 10
            summation += node.value
        return self.most_significant_value(summation)

    def remove_intercalary_domain(self, node_domain):
        sum_values = node_domain[self.adjacent_nodes[0]]
        for i in range(1, len(self.adjacent_nodes)):
            new_sum_values = []
            for v in sum_values:
                for q in node_domain[self.adjacent_nodes[i]]:
                    new_sum_values.append(v + q)
            sum_values = new_sum_values
        possible_value = set()
        for value in sum_values:
            possible_value.add(self.most_significant_value(value))

        possible_value = list(possible_value)
        node_domain[self] = [v for v in node_domain[self] if v in possible_value]
    