from collections import deque


def BFS(arr, start):
    # Проверка, не пустой ли граф
    if len(arr) == 0:
        return []

    deq = deque()  # Создаём очередь для хранения вершин, в которые можно попасть
    result = list()
    deq.append(start)

    used = [False] * len(arr)  # Создаём список посещений вершин: True - вершину посетили, False - нет
    used[start] = True
    
    # Пока есть вершины, в которые можно попасть, будет осуществляться обход графа
    while len(deq) > 0:
        point_now = deq.popleft()  # Добавление текущей вершины в список
        result.append(point_now)

        for i in arr[point_now]:  # Проход по всем вершинам, инцидентным текущей
            
            if not used[i]:  # Если вершина ещё не была посещена, добавляем её в конец очереди
                deq.append(i)
                used[i] = True
    return result


if __name__ == '__main__':
    print(BFS.__doc__)
