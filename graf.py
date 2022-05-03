import bfs
import dfs
import bestTopSort

if __name__ == '__main__':
    print("Введите количество вершин")
    g = [[] for i in range(int(input()))]
    n = int(input())
    for i in range(n):
        f, s = map(int, input().split())
        g[f].append(s)
    k = bestTopSort.topological_sort(g)
    print(*k)
