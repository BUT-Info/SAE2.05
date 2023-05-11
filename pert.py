import networkx as nx
from random import randint
from typing import Dict
import matplotlib.pyplot as plt

pert = nx.DiGraph()
"""pert.add_node('A', duration=3)
pert.add_node('B', duration=4)
pert.add_node('C', duration=8)
pert.add_node('D', duration=6)
pert.add_node('E', duration=2)
pert.add_node('F', duration=10)
pert.add_node('G', duration=5)
pert.add_node('H', duration=3)
pert.add_node('I', duration=2)
pert.add_node('J', duration=4)
pert.add_node('K', duration=4)
pert.add_node('L', duration=4)
pert.add_node('M', duration=10)
pert.add_edge('A', 'C')
pert.add_edge('B', 'D')
pert.add_edge('C', 'D')
pert.add_edge('D', 'E')
pert.add_edge('D', 'F')
pert.add_edge('F', 'G')
pert.add_edge('D', 'H')
pert.add_edge('E', 'I')
pert.add_edge('C', 'J')
pert.add_edge('B', 'J')
pert.add_edge('G', 'K')
pert.add_edge('H', 'K')
pert.add_edge('I', 'L')
pert.add_edge('J', 'L')
pert.add_edge('K', 'L')
pert.add_edge('L', 'M')"""
pert.add_edge('A', 'B')
pert.add_edge('B', 'C')
pert.add_edge('B', 'D')
pert.add_edge('C', 'E')
pert.add_edge('D', 'E')
pert.add_edge('E', 'I')
pert.add_edge('I', 'J')
pert.add_edge('J', 'K')
pert.add_edge('I', 'G')
pert.add_edge('G', 'J')

for task in pert.nodes:
    pert.nodes[task]['duration'] = randint(1, 10)

layout = nx.nx_pydot.graphviz_layout(pert, prog='dot')
nx.draw(pert, pos=layout)
nx.draw_networkx_labels(pert, pos=layout)

labels = {}
for task in pert.nodes:
    for edge in pert.out_edges(task):
        labels[edge] = pert.nodes[task]['duration']

nx.draw_networkx_edge_labels(pert, pos=layout, edge_labels=labels)
plt.show()

sources = [task for task in pert.nodes if pert.in_degree(task) == 0]
puits = [task for task in pert.nodes if pert.out_degree(task) == 0]

asap: Dict[str, str] = dict()
for source in sources:
    asap[source] = pert.nodes[source]['duration']

frontiere = []
for task in sources:
    frontiere.extend(pert.successors(task))

while len(frontiere):
    sucessors = []
    for task in frontiere:
        start = 0
        for predecessor in pert.predecessors(task):
            start = max(start, asap[predecessor])
        asap[task] = start + pert.nodes[task]['duration']
        sucessors.extend(pert.successors(task))
    frontiere = sucessors

m = 0
for task in pert.nodes:
    m = max(asap[task], m)

alap: Dict[str, str] = dict()
for puit in puits:
    alap[puit] = m

frontiere = []
for task in puits:
    frontiere.extend(pert.predecessors(task))

while len(frontiere):
    predecessors = []
    for task in frontiere:
        end = m
        for successor in pert.successors(task):
            end = min(end, alap[successor] - pert.nodes[successor]['duration'])
        alap[task] = end - pert.nodes[task]['duration']
        predecessors.extend(pert.predecessors(task))
    frontiere = predecessors

print(pert)
print(asap)
print(alap)

for task in pert.nodes:
    duration = pert.nodes[task]['duration']
    print(task, '|', '-'.join(pert.predecessors(task)), '|', asap[task] - duration, asap[task], '|')#, alap[task] - duration, alap[task], '|', alap[task] - asap[task])
