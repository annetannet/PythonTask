def TopologicalSort(graph):
    """

    Упорядочивание вершин ацикличного графа таким образом, что для любого ребра (u,v) номер вершины u меньше номера вершины v

    :param graph: ацикличный граф
    :return: список упорядоченных вершин
    """
    # Создать словарь степеней
    degree = dict()
    for node in range(len(graph)):
        degree[node] = 0
    # Получить степень каждого узла
    for node in graph:
        for connected_node in node:
            degree[connected_node] += 1
    # Использовать список в качестве очереди и добавить вершины со степенью 0 в очередь
    queue = [node for node in range(len(graph)) if degree[node] == 0]
    result = []
    # Выполняется при наличии элементов в очереди
    while queue:
        # Удалить вершину из очереди
        node = queue.pop()
        # Сохранить полученную вершину в результате
        result.append(node)
        # Уменьшить степени всех вершин, на которые указывала удалённая
        for connected_node in graph[node]:
            degree[connected_node] -= 1
            # Если удаленная вершина (u) указывала на вершину степени 0 (v), v добавляется в очередь
            if degree[connected_node] == 0:
                queue.append(connected_node)
    return result


if __name__ == '__main__':
    # print(TopologicalSort.__doc__)
    print(TopologicalSort([[1, 2], [3, 4], [3, 4], [5], [5], []]))
