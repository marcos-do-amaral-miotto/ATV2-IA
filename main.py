import networkx as nx
import random
import time
import matplotlib.pyplot as plt


def generate_graph(num_vertices, num_edges):
    G = nx.Graph()
    G.add_nodes_from(range(num_vertices))

    for node in range(num_vertices):
        edges = random.sample(range(num_vertices), num_edges)
        for edge in edges:
            if node != edge:
                G.add_edge(node, edge)

    return G


def bfs(graph, start, goal):
    start_time = time.time()
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor == goal:
                end_time = time.time()
                return path + [neighbor], end_time - start_time
            else:
                queue.append((neighbor, path + [neighbor]))
    return None, None


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


if __name__ == "__main__":
    parameters = [(500, 3), (500, 5), (500, 7), (5000, 3), (5000, 5), (5000, 7), (10000, 3), (10000, 5), (10000, 7)]
    results = []

    for vertices, edges in parameters:
        graph = generate_graph(vertices, edges)
        start, goal = random.choice(list(graph.nodes)), random.choice(list(graph.nodes))

        path_bfs, time_bfs = bfs(graph, start, goal)
        path_dfs, time_dfs = dfs(graph, start, goal)
        path_dls = depth_limited_search(graph, start, goal, limit=10)

        results.append((vertices, edges, start, goal, len(path_bfs) if path_bfs else None, time_bfs,
                        len(path_dfs) if path_dfs else None, time_dfs,
                        len(path_dls) if path_dls else None))

    for res in results:
        print(f"Vértices: {res[0]}, Arestas: {res[1]}, Início: {res[2]}, Fim: {res[3]}\n"
              f"BFS - Caminho: {res[4]}, Tempo: {res[5]:.6f}s\n"
              f"DFS - Caminho: {res[6]}, Tempo: {res[7]:.6f}s\n"
              f"DLS - Caminho: {res[8]}\n")
