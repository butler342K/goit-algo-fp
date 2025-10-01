import heapq

import networkx as nx
import matplotlib.pyplot as plt


# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    visited = set()
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_path, current = heapq.heappop(priority_queue)               
        if current in visited:
            continue
        visited.add(current)
        for neighbor, weight in graph[current].items():
            distance = current_path + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return shortest_paths

def main():
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4, 'F': 1},
        'F': {'E': 1,'B': 9}
    }
    # Використання алгоритму Дейкстри
    start_vertex = "A"

    shortest_paths = dijkstra(graph, start_vertex)
    print(shortest_paths)

    # Візуалізація графа
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    node_colors = ['coral' if node == start_vertex else 'lightblue' for node in G.nodes()]
    pos = nx.spring_layout(G)  # Positions for all nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_colors)
    nx.draw_networkx_edges(G, pos, width=2)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

    plt.axis("off")

    plt.title('Найкоротші шляхи\n' + str(shortest_paths), 
         fontsize=14)
    
    plt.show()

if __name__ == "__main__":
    main()