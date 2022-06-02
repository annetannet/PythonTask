import heapq
import graph_generator


def Dijkstra(graph, start):
    """
    Алгоритм поиска, использующийся для определения кратчайшего пути между двумя узлами в графе
    :param graph: граф (список списков таплов)
    :param start: начальный узел в формате (вес, индекс узла)
    :return:
    """
    # Проверка, не пустой ли граф
    if len(graph) == 0:
        return []
    q = []
    heapq.heappush(q, start)
    cost = [0] * len(graph)  # Сохраняет вес с которым переходим в i-ую вершину
    # Повторяем до тех пор, пока не посетим все узлы графа
    while len(q) > 0:
        # Выбираем узел с наименьшим значением в качестве «текущего узла» и посещаем всех соседей
        point_now = heapq.heappop(q)[1]
        neighbours = graph[point_now]  # graph[point_now] = [(weight_1, neighbour_1), (weight_2, neighbour_2), ...]
        for i in neighbours:
            if cost[i[1]] == 0 \
                    or cost[i[1]] > cost[point_now] + i[0]:
                heapq.heappush(q, i)
                # При посещении каждого узла, обновляем его расстояние от начального узла
                cost[i[1]] = cost[point_now] + i[0]
    return cost
if __name__ == "__main__":
    best_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.best_graph(550), 2)
    worst_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.worst_graph(30), 2)
    rnd_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.random_graph(50), 2)
    print(Dijkstra(rnd_weighted_graph_8KB, (0, 0)))
