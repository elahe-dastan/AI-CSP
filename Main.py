from Algorithm import Algorithm
from Circle import Circle
from Hexagon import Hexagon
from Pentagon import Pentagon
from Square import Square
from Triangle import Triangle

V = input()
E = input()
input_nodes = input().split()
nodes = []
edges = []
for i in range(int(E)):
    edges.append(input())

for input in input_nodes:
    if input == "C":
        nodes.append(Circle())
    elif input == "P":
        nodes.append(Pentagon())
    elif input == "H":
        nodes.append(Hexagon())
    elif input == "S":
        nodes.append(Square())
    else:
        nodes.append(Triangle())

for edge in edges:
    adjacent_nodes = edge.split()
    first_node = nodes[int(adjacent_nodes[0])]
    second_node = nodes[int(adjacent_nodes[1])]
    first_node.add_adjacent_node(second_node)
    second_node.add_adjacent_node(first_node)

node_domain = {}
for node in nodes:
    domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    node_domain[node] = domain

algorithm = Algorithm(node_domain)
# result = algorithm.bt_fc_search({}, node_domain)
result = algorithm.bt_fc_mrv({}, node_domain)
print(result)

