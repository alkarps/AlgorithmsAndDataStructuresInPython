# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

def test_dfs(fun):
    test_graph = [[1, 2], [0, 3, 4], [0], [1], [2, 3]]
    assert {0, 1, 2, 3, 4} == fun(test_graph, 0)


def input_count_node():
    while True:
        n = input("Введите количество вершин: ")
        if n.isdigit():
            n = int(n)
            if n > 0:
                return n
        print("Ошибка ввода количества вершин")


def input_graph_edge_for_node(i, count_nodes):
    while True:
        edges = []
        input_edges = input(f"Введите связанные вершины для вершины {i + 1} через запятую: ")
        if input_edges.isspace() or len(input_edges) == 0:
            return edges
        for _edge in input_edges.split(","):
            if not _edge.isdigit() or not (0 <= int(_edge) - 1 < count_nodes):
                break
            else:
                edges.append(int(_edge) - 1)
        else:
            return edges
        print("Ошибка ввода количества вершин")


def input_graph():
    n = input_count_node()
    graph = []
    for i in range(n):
        graph.append(input_graph_edge_for_node(i, n))
    return graph


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in set(graph[start]) - visited:
        dfs(graph, next, visited)
    return visited


if __name__ == "__main__":
    test_dfs(dfs)
    input_graph = input_graph()
    print(dfs(input_graph, 0))
