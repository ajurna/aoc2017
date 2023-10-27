from dataclasses import dataclass, field
from typing import Optional, List
from collections import Counter

nodes = {}


@dataclass
class Node:
    name: str
    weight: int = 0
    children: List[str] = field(default_factory=list)
    parent: Optional["Node"] = None

    @property
    def get_weight(self):
        if self.children:
            return sum([nodes[c].get_weight for c in self.children]) + self.weight
        return self.weight

    def children_balanced(self):
        weights = [nodes[c].get_weight for c in self.children]
        weight = weights[0]
        return  all(w==weight for w in weights)


with open('01.txt') as f:
    for line in f.readlines():
        if '->' in line:
            parent, children = line.split(' -> ')
            name, weight = parent.strip().split(' (')
            children = children.strip().split(', ')
            if name in nodes:
                node = nodes[name]
            else:
                node = Node(name)
                nodes[name] = node
            node.weight = int(weight[:-1])
            node.children = children
            for child in node.children:
                if child in nodes:
                    child_node = nodes[child]
                else:
                    child_node = Node(name)
                    nodes[child] = child_node
                child_node.parent = node.name
        else:
            name, weight = line.strip().split(' (')
            if name in nodes:
                node = nodes[name]
            else:
                node = Node(name)
                nodes[name] = node
            node.weight = int(weight[:-1])


def find_unbalanced_node(node: Node):
    if node.children_balanced():
        return node
    else:
        weights = [nodes[c].get_weight for c in node.children]
        unbalanced_weight = [k for k,v in Counter(weights).items() if v == 1][0]
        unbalanced_node_name = node.children[weights.index(unbalanced_weight)]
        unbalanced_node = nodes[unbalanced_node_name]
        return find_unbalanced_node(unbalanced_node)


node = list(nodes.values())[0]
while node.parent:
    node = nodes[node.parent]
print("Part 1:", node.name)

child_weights = [nodes[c].get_weight for c in node.children]
diff = max(child_weights) - min(child_weights)

print("Part 2:", find_unbalanced_node(node).weight - diff)
