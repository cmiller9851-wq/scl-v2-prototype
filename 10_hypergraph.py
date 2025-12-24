import networkx as nx
import hashlib
from copy import deepcopy

class L0Hypergraph:
    def __init__(self, graph=None):
        if graph is None:
            self.G = nx.MultiDiGraph()
        else:
            self.G = graph
        self.freeze()
        self.version = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        graph_data = nx.to_dict_of_dicts(self.G)
        serialized = str(sorted(graph_data.items())).encode()
        return hashlib.sha256(serialized).hexdigest()

    def freeze(self):
        self.G = nx.freeze(self.G)

    def add_node(self, node_id, data):
        new_G = deepcopy(self.G)
        new_G.add_node(node_id, data=data)
        return L0Hypergraph(new_G)

    def add_edge(self, source, target, relation):
        new_G = deepcopy(self.G)
        new_G.add_edge(source, target, relation=relation)
        return L0Hypergraph(new_G)

    def get_hash(self):
        return self.hash

    def get_version(self):
        return self.version