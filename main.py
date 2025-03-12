import networkx as nx
import random
import time


def criar_grafo_ponderado(qtd_vertices, qtd_arestas):
    grafo = nx.Graph()
    grafo.add_nodes_from(range(qtd_vertices))

    for vertice in range(qtd_vertices):
        vizinhos = random.sample(range(qtd_vertices), min(qtd_arestas, qtd_vertices - 1))
        for vizinho in vizinhos:
            if vertice != vizinho:
                peso = random.randint(1, 10)
                grafo.add_edge(vertice, vizinho, weight=peso)

    return grafo


def busca_em_largura(grafo, inicio, destino):
    inicio_tempo = time.time()
    fila = [(inicio, [inicio])]
    visitados = set()

    while fila:
        no_atual, caminho = fila.pop(0)
        if no_atual in visitados:
            continue
        visitados.add(no_atual)

        for vizinho in grafo[no_atual]:
            if vizinho == destino:
                return caminho + [vizinho], time.time() - inicio_tempo
            fila.append((vizinho, caminho + [vizinho]))

    return None, None


def busca_em_profundidade(grafo, inicio, destino, caminho=None, visitados=None, inicio_tempo=None, limite=500):
    if caminho is None:
        caminho = [inicio]
    if visitados is None:
        visitados = set()
    if inicio_tempo is None:
        inicio_tempo = time.time()
    if limite <= 0:
        return None, None

    visitados.add(inicio)
    if inicio == destino:
        return caminho, time.time() - inicio_tempo

    for vizinho in grafo.neighbors(inicio):
        if vizinho not in visitados:
            resultado, tempo_exec = busca_em_profundidade(grafo, vizinho, destino, caminho + [vizinho], visitados, inicio_tempo, limite - 1)
            if resultado:
                return resultado, tempo_exec

    return None, None


def busca_limitada(grafo, inicio, destino, limite, caminho=None):
    if caminho is None:
        caminho = [inicio]
    if inicio == destino:
        return caminho
    if limite <= 0:
        return None

    for vizinho in grafo.neighbors(inicio):
        if vizinho not in caminho:
            novo_caminho = busca_limitada(grafo, vizinho, destino, limite - 1, caminho + [vizinho])
            if novo_caminho:
                return novo_caminho

    return None


if __name__ == "__main__":
    parametros = [(500, 3), (500, 5), (500, 7), (5000, 3), (5000, 5), (5000, 7), (10000, 3), (10000, 5), (10000, 7)]

    for vertices, arestas in parametros:
        grafo = criar_grafo_ponderado(vertices, arestas)
        origem, destino = random.sample(list(grafo.nodes), 2)

        caminho_bfs, tempo_bfs = busca_em_largura(grafo, origem, destino)
        caminho_dfs, tempo_dfs = busca_em_profundidade(grafo, origem, destino)
        caminho_dls = busca_limitada(grafo, origem, destino, limite=10)

        print(f"\nGrafo com {vertices} vértices e {arestas} arestas por vértice")
        print(f"Origem: {origem}, Destino: {destino}")

        if caminho_bfs:
            print(f"BFS - Caminho encontrado ({len(caminho_bfs)} nós), Tempo: {tempo_bfs:.6f}s")
            print(f"Caminho: {caminho_bfs}")
        else:
            print("BFS - Caminho não encontrado")

        if caminho_dfs:
            print(f"DFS - Caminho encontrado ({len(caminho_dfs)} nós), Tempo: {tempo_dfs:.6f}s")
            print(f"Caminho: {caminho_dfs}")
        else:
            print("DFS - Caminho não encontrado")

        if caminho_dls:
            print(f"DLS - Caminho encontrado ({len(caminho_dls)} nós)")
            print(f"Caminho: {caminho_dls}")
        else:
            print("DLS - Caminho não encontrado")

        print("-" * 50)
