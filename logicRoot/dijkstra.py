import heapq
from logicRoot.graph import Graph

def dijkstra(graph, start, end):
    if start not in graph.nodes or end not in graph.nodes:
        raise ValueError("Start sau end nu sunt în graf.")

    distances = {node: float('infinity') for node in graph.nodes}
    previous_nodes = {}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            path = []
            while current_node in previous_nodes:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            return [start] + path

        for neighbor, weight in graph.nodes[current_node].adjacent.items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return None