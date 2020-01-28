from Node import Node


class Square(Node):
    def unique_satisfiable_value(self):
        multiplication = self.multiplication_of_neighbours_value()
        if multiplication is None:
            return None
        return self.least_significant_value(multiplication)

    def remove_intercalary_domain(self, node_domain):
        mul_values = self.combinational_multiplication_of_domain_of_neighbours(node_domain)
        self.shorten_domain_least_significant_digit(node_domain, mul_values)

