import csv
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, Tuple

pert = nx.DiGraph()

with open('tasks-sae.csv') as csvfile:
    tasks = list(csv.reader(csvfile, delimiter=','))
    for task, duration, predecessors, label, _ in tasks:
        pert.add_node(task, duration=int(duration))
    
    for task, duration, predecessors, label, _ in tasks:
        if predecessors == '':
            continue
        for predecessor in predecessors.split('-'):
            pert.add_edge(predecessor, task)

layout = nx.nx_pydot.graphviz_layout(pert, prog='dot')
nx.draw(pert, pos=layout)
nx.draw_networkx_labels(pert, pos=layout)

labels: Dict[Tuple[str, str], int] = {}
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
        stop = False
        for predecessor in pert.predecessors(task):
            if predecessor not in asap:
                stop = True
                break
            start = max(start, asap[predecessor])
        if stop:
            continue
        asap[task] = start + pert.nodes[task]['duration']
        sucessors.extend(pert.successors(task))
    frontiere = sucessors

total_duration = 0
for task in pert.nodes:
    total_duration = max(asap[task], total_duration)

alap: Dict[str, str] = dict()
for puit in puits:
    alap[puit] = total_duration - pert.nodes[puit]['duration']

frontiere = []
for task in puits:
    frontiere.extend(pert.predecessors(task))

while len(frontiere):
    predecessors = []
    for task in frontiere:
        end = total_duration
        stop = False
        for successor in pert.successors(task):
            if successor not in alap:
                stop = True
                break
            end = min(end, alap[successor])
        if stop:
            continue
        alap[task] = end - pert.nodes[task]['duration']
        predecessors.extend(pert.predecessors(task))
    frontiere = predecessors

print('Durée totale :', total_duration, 'heures')
for task in pert.nodes:
    duration = pert.nodes[task]['duration']
    print('|', task, '|', duration, '|', '-'.join(pert.predecessors(task)), '|', asap[task] - duration, '|', asap[task], '|', alap[task], '|', alap[task] + duration, '|', alap[task] + duration - asap[task], '|', sep='')


nrow = pert.number_of_nodes()
plt.figure()
bar_width = 0.9

tasks = list(pert.nodes)

for i, task in enumerate(reversed(tasks)):
    duration = pert.nodes[task]['duration']
    plt.broken_barh([(asap[task] - duration, duration)], (i - bar_width / 2, bar_width))
    #plt.broken_barh([(asap[task], alap[task] - asap[task])], (i - bar_width / 2, bar_width), color='green')

plt.yticks([i for i in range(nrow)], reversed(tasks))

plt.show()
