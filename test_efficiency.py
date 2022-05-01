import functools
import time
import dfs
import bfs
import dikstra
import top_sort
import bestTopSort


def logging(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        for i in range(1, 100000):
            function(*args)
        end_time = time.time()
        work_time = (end_time - start_time)
        print(work_time, end = "\n\n")
    return wrapper


@logging
def speedDfs(graph, start):
    return dfs.DFS(graph, start)
@logging
def speedBfs(a, start):
    return bfs.BFS(a, start)
@logging
def speedTop_sort(a):
    return top_sort.TopologicalSort(a)
@logging
def speedTop_sortAnother(a):
    return bestTopSort.topological_sort(a)
@logging
def speedDikstra(a, start):
    return dikstra.Dijkstra(a, start)

if __name__ == '__main__':
    a = [[1, 2, 3, 4], [4], [], [], []]
    print("DFS на ацикличном графе")
    print("Time: ", end = ' ')
    speedDfs(a, 0)
    print("DFS на цикличном графе")
    print("Time: ", end = ' ')
    speedDfs([[1],[2],[0]], 0)
    print("BFS на ацикличном графе")
    print("Time: ", end = ' ')
    speedBfs(a, 0)
    print("BFS на цикличном графе")
    print("Time: ", end = ' ')
    speedBfs([[1],[2],[0]], 0)
    print("Topological sort алгоритм Кана")
    print("Time: ", end = ' ')
    speedTop_sort(a)
    print("Topological sort алгоритм основаный на DFS")
    print("Time: ", end = ' ')
    speedTop_sortAnother(a)
    print("Диикстра sort алгоритм основаный на DFS")
    print("Time: ", end = ' ')
    speedDikstra([[(1,1),(2,2)],[(3,3)],[(4,3)],[]], 0)