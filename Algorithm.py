def forward_checking(node, node_domain):
    for adjacent_node in node.adjacent_nodes:
        if adjacent_node.value == 0:
            adjacent_node.remove_intercalary_domain(node_domain)


def find_node_mrv(nodes, node_domain):
    min_domain_length = 10
    selected_node = True
    for node in nodes:
        if len(node_domain[node]) < min_domain_length:
            min_domain_length = len(node_domain[node])
            selected_node = node
    return selected_node


def consistent(assignment):
    for node in assignment:
        if not node.value_satisfiable():
            return False
    return True


class Algorithm:
    def __init__(self, node_domain):
        self.node_domain = node_domain

    def bt_fc_search(self, assignment, node_domain_local):
        if len(assignment) == len(self.node_domain):
            return assignment
        unassigned = [v for v in self.node_domain.keys() if v not in assignment]
        first = unassigned[0]
        for value in node_domain_local[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            first.value = value
            if consistent(local_assignment):
                node_domain_copy = node_domain_local.copy()
                node_domain_copy[first] = [value]
                forward_checking(first, node_domain_copy)
                result = self.bt_fc_search(local_assignment, node_domain_copy)
                if result is not None:
                    return result
        first.value = 0
        return None

    def bt_fc_mrv(self, assignment, node_domain_local):
        if len(assignment) == len(self.node_domain):
            return assignment
        unassigned = [v for v in self.node_domain.keys() if v not in assignment]
        first = find_node_mrv(unassigned, node_domain_local)
        for value in node_domain_local[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            first.value = value
            if consistent(local_assignment):
                node_domain_copy = node_domain_local.copy()
                node_domain_copy[first] = [value]
                forward_checking(first, node_domain_copy)
                result = self.bt_fc_mrv(local_assignment, node_domain_copy)
                if result is not None:
                    return result
        first.value = 0
        return None

