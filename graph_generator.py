import random


def random_graph(count):
    g = [[] for _ in range(count)]
    for i in range(count):
        k = random.randint(0, count - 1)
        for j in range(k):
            r = random.randint(0, count - 1)
            if r != i:
                g[i].append(r)
        g[i] = list(set(g[i]))
    return g


def best_graph(count):
    g = [[] for _ in range(count)]
    for i in range(1, count):
        g[0].append(i)
    return g


def worst_graph(count):
    g = [[] for _ in range(count)]
    for i in range(count):
        for j in range(count):
            if i != j:
                g[i].append(j)
    return g


def weighted_graph(graph, max_weight):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] = (random.randint(0, max_weight), graph[i][j])
    return graph


if __name__ == '__main__':
    print(weighted_graph(random_graph(3), 3))
    # b = weighted_graph(random_graph(100), 2).__str__()
    # with open('test_graph', 'w') as tg:
    #     tg.write(b.__str__())
