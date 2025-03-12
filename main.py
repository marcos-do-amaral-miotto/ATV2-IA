import networkx as nx
import random
import time
import matplotlib.pyplot as plt
import numpy as np


def generate_weighted_graph(num_vertices, num_edges):
    G = nx.Graph()
    G.add_nodes_from(range(num_vertices))

    for node in range(num_vertices):
        edges = random.sample(range(num_vertices), num_edges)
        for edge in edges:
            if node != edge:
                weight = random.randint(1, 10)  # Arestas com pesos aleatórios
                G.add_edge(node, edge, weight=weight)

    return G


def bfs(graph, start, goal):
    start_time = time.time()
    queue = [(start, [start])]
    visited = set()
    path_found = None

    while queue:
        (vertex, path) = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor == goal:
                end_time = time.time()
                path_found = path + [neighbor]
                return path_found, end_time - start_time
            else:
                queue.append((neighbor, path + [neighbor]))
    return path_found, None


def dfs(graph, start, goal, path=None, visited=None, start_time=None, depth_limit=500):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    if start_time is None:
        start_time = time.time()
    if depth_limit <= 0:
        return None, None

    visited.add(start)
    if start == goal:
        return path, time.time() - start_time

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result, exec_time = dfs(graph, neighbor, goal, path + [neighbor], visited, start_time, depth_limit - 1)
            if result is not None:
                return result, exec_time

    return None, None


def depth_limited_search(graph, start, goal, limit, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    if limit <= 0:
        return None

    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = depth_limited_search(graph, neighbor, goal, limit - 1, path + [neighbor])
            if new_path:
                return new_path

    return None


def plot_graph(graph, path=None):
    pos = nx.spring_layout(graph, seed=42)  # Usar uma semente fixa para garantir layout consistente
    plt.figure(figsize=(10, 8))

    # Desenhando o grafo
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=12, font_weight="bold", edge_color='gray', alpha=0.6)

    # Destacando as arestas do caminho em vermelho
    if path:
        edges_in_path = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(graph, pos, edgelist=edges_in_path, edge_color='red', width=2, alpha=0.8)

    # Desenhando os pesos das arestas de forma destacada
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10, font_color='black')

    # Ajustando o título
    plt.title("Visualização do Grafo com Caminho Destacado", fontsize=16)
    plt.axis('off')  # Desligando os eixos para uma visualização mais limpa
    plt.show()


if __name__ == "__main__":
    parameters = [(500, 3), (500, 5), (500, 7), (5000, 3), (5000, 5), (5000, 7), (10000, 3), (10000, 5), (10000, 7)]
    results = []

    for vertices, edges in parameters:
        graph = generate_weighted_graph(vertices, edges)
        start, goal = random.choice(list(graph.nodes)), random.choice(list(graph.nodes))

        # Buscas
        path_bfs, time_bfs = bfs(graph, start, goal)
        path_dfs, time_dfs = dfs(graph, start, goal)
        path_dls = depth_limited_search(graph, start, goal, limit=10)

        # Visualização do comportamento
        if path_bfs:
            print(f"BFS - Caminho: {path_bfs}, Tempo: {time_bfs:.6f}s")
            plot_graph(graph, path_bfs)
        if path_dfs:
            print(f"DFS - Caminho: {path_dfs}, Tempo: {time_dfs:.6f}s")
            plot_graph(graph, path_dfs)
        if path_dls:
            print(f"DLS - Caminho: {path_dls}")
            plot_graph(graph, path_dls)

        # Armazenar os resultados
        results.append((vertices, edges, start, goal, len(path_bfs) if path_bfs else None, time_bfs,
                        len(path_dfs) if path_dfs else None, time_dfs,
                        len(path_dls) if path_dls else None))

    for res in results:
        print(f"Vértices: {res[0]}, Arestas: {res[1]}, Início: {res[2]}, Fim: {res[3]}\n"
              f"BFS - Caminho: {res[4]}, Tempo: {res[5]:.6f}s\n"
              f"DFS - Caminho: {res[6]}, Tempo: {res[7]:.6f}s\n"
              f"DLS - Caminho: {res[8]}\n")
