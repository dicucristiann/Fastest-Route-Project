from logicRoot.node import Node

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        """Adaugam un nod in graf daca acesta nu exista deja."""
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def add_edge(self, from_node, to_node, weight):
        """Adaugam o muchie intre doua noduri cu o greutate specificata."""
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node].add_edge(to_node, weight)
        else:
            raise ValueError("Unul sau ambele noduri nu exista în graf.")

    def get_node(self, name):
        """Returneaza nodul cu numele specificat din graf."""
        if name in self.nodes:
            return self.nodes[name]
        else:
            raise ValueError(f"Nodul '{name}' nu exista în graf.")

    def __str__(self):
        """Returneaza o reprezentare string a graficului."""
        return '\n'.join([f'{node}: {self.nodes[node].adjacent}' for node in self.nodes])
