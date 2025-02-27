# Atividade 2 - Busca Não Informada

Este projeto implementa algoritmos de busca não informada para grafos, incluindo busca em largura (BFS), busca em profundidade (DFS) e busca em profundidade limitada (DLS). O objetivo é testar o desempenho dessas buscas em diferentes configurações de grafos e analisar os tempos de execução e os caminhos encontrados.

## Requisitos da Atividade

De acordo com o enunciado da atividade, foram implementadas as seguintes funcionalidades:

- Geração de grafos aleatórios com combinações de:
  - Número de vértices (v) = 500, 5000, 10000
  - Número de arestas (k) = 3, 5, 7
- Implementação dos algoritmos de busca:
  - Busca em Largura (BFS)
  - Busca em Profundidade (DFS)
  - Busca em Profundidade Limitada (DLS)
- Teste das buscas em encontrar um caminho entre um ponto inicial e um final previamente definidos.
- Coleta de métricas:
  - Ponto inicial e final de cada grafo
  - Caminho encontrado por cada algoritmo
  - Tempo de execução de cada algoritmo
  - Tamanho do caminho encontrado
- Geração de um grafo Kn com v = 10000 para análise do comportamento dos algoritmos.

## Estrutura do Projeto

- `main.py`: Código principal que gera os grafos, executa os algoritmos de busca e coleta os resultados.
- `requirements.txt`: Lista de dependências necessárias para rodar o projeto.
- `README.md`: Este documento explicando o funcionamento do projeto.

## Como Executar o Código

1. Instale as dependências necessárias:
   ```sh
   pip install -r requirements.txt
   ```
2. Execute o script principal:
   ```sh
   python main.py
   ```
3. O script irá gerar grafos e rodar os algoritmos, exibindo os resultados no console.

## Tecnologias Utilizadas

- Python 3
- NetworkX (para manipulação de grafos)
- Matplotlib (para visualização dos grafos, se necessário)


