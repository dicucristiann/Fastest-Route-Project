class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = {}

    def add_edge(self, neighbor, weight):
        if neighbor not in self.adjacent or weight < self.adjacent[neighbor]:
            self.adjacent[neighbor] = weight