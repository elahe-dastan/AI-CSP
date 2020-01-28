from Node import Node


class Hexagon(Node):
    def unique_satisfiable_value(self):
        summation = self.summation_of_neighbours_value()
        if summation is None:
            return None
        return self.least_significant_value(summation)

    def remove_intercalary_domain(self, node_domain):
        sum_values = self.combinational_summation_of_domain_of_neighbours(node_domain)
        self.shorten_domain_least_significant_digit(node_domain, sum_values)