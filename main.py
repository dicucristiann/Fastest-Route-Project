from logicRoot.graph import Graph
from logicRoot.dijkstra import dijkstra
from logicRoot.data import nodes, edges


def main():
    graph = Graph()

    # Adaugam Date Generale din data.py
    for node in nodes:
        graph.add_node(node)

    for from_node, to_node, weight in edges:
        graph.add_edge(from_node, to_node, weight)

    start, end = 'Bucuresti', 'Cluj-Napoca'
    try:
        path = dijkstra(graph, start, end)
        print("Cel mai scurt drum este:", path)
    except ValueError as e:
        print("Eroare:", e)


if __name__ == "__main__":
    main()
