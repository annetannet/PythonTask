import functools
import dfs
import bfs
import dikstra
import top_sort
import top_sort_DFS
import sys
import graph_generator


def logging(function):
    @functools.wraps(function)
    def wrapper(*args):
        k = sys.getsizeof(function(*args))  # bytes
        print(k, end="\n\n")
    return wrapper


@logging
def mem_dfs(graph, start):
    return dfs.DFS(graph, start)


@logging
def mem_bfs(a, start):
    return bfs.BFS(a, start)


@logging
def mem_top_sort_Kahn(a):
    return top_sort.TopologicalSort(a)


@logging
def mem_top_sort_DFS(a):
    return top_sort_DFS.DFS(a)


@logging
def mem_dijkstra(a, start):
    return dikstra.Dijkstra(a, start)


if __name__ == '__main__':
    best_data_8KB = graph_generator.best_graph(900)
    best_data_16KB = graph_generator.best_graph(1700)
    best_data_32KB = graph_generator.best_graph(3350)
    worst_data_8KB = graph_generator.worst_graph(45)
    worst_data_16KB = graph_generator.worst_graph(65)
    worst_data_32KB = graph_generator.worst_graph(92)
    rnd_data_8KB = graph_generator.random_graph(75)
    rnd_data_16KB = graph_generator.random_graph(105)
    rnd_data_32KB = graph_generator.random_graph(140)
    # best_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.best_graph(550), 2)
    # worst_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.worst_graph(30), 2)
    # rnd_weighted_graph_8KB = graph_generator.weighted_graph(graph_generator.random_graph(50), 2)
    # best_weighted_graph_16KB = graph_generator.weighted_graph(graph_generator.best_graph(1100), 2)
    # worst_weighted_graph_16KB = graph_generator.weighted_graph(graph_generator.worst_graph(43), 2)
    # rnd_weighted_graph_16KB = graph_generator.weighted_graph(graph_generator.random_graph(71), 2)
    # best_weighted_graph_32KB = graph_generator.weighted_graph(graph_generator.best_graph(2200), 2)
    # worst_weighted_graph_32KB = graph_generator.weighted_graph(graph_generator.worst_graph(61), 2)
    # rnd_weighted_graph_32KB = graph_generator.weighted_graph(graph_generator.random_graph(100), 2)
    print("DFS")
    mem_dfs(best_data_8KB, 0)
    mem_dfs(worst_data_8KB, 0)
    mem_dfs(rnd_data_8KB, 0)
    mem_dfs(best_data_16KB, 0)
    mem_dfs(worst_data_16KB, 0)
    mem_dfs(rnd_data_16KB, 0)
    mem_dfs(best_data_32KB, 0)
    mem_dfs(worst_data_32KB, 0)
    mem_dfs(rnd_data_32KB, 0)
    print("BFS")
    mem_bfs(best_data_8KB, 0)
    mem_bfs(worst_data_8KB, 0)
    mem_bfs(rnd_data_8KB, 0)
    mem_bfs(best_data_16KB, 0)
    mem_bfs(worst_data_16KB, 0)
    mem_bfs(rnd_data_16KB, 0)
    mem_bfs(best_data_32KB, 0)
    mem_bfs(worst_data_32KB, 0)
    mem_bfs(rnd_data_32KB, 0)
    print("Topological sort by Kahn")
    mem_top_sort_Kahn(best_data_8KB)
    mem_top_sort_Kahn(worst_data_8KB)
    mem_top_sort_Kahn(rnd_data_8KB)
    mem_top_sort_Kahn(best_data_16KB)
    mem_top_sort_Kahn(worst_data_16KB)
    mem_top_sort_Kahn(rnd_data_16KB)
    mem_top_sort_Kahn(best_data_32KB)
    mem_top_sort_Kahn(worst_data_32KB)
    mem_top_sort_Kahn(rnd_data_32KB)
    print("Topological sort on DFS")
    mem_top_sort_DFS(best_data_8KB)
    mem_top_sort_DFS(worst_data_8KB)
    mem_top_sort_DFS(rnd_data_8KB)
    mem_top_sort_DFS(best_data_16KB)
    mem_top_sort_DFS(worst_data_16KB)
    mem_top_sort_DFS(rnd_data_16KB)
    mem_top_sort_DFS(best_data_32KB)
    mem_top_sort_DFS(worst_data_32KB)
    mem_top_sort_DFS(rnd_data_32KB)
    # print("Dijkstra")
    # mem_dijkstra(best_weighted_graph_8KB, (0, 0))
    # mem_dijkstra(worst_weighted_graph_8KB, (0, 0))
    # mem_dijkstra(rnd_weighted_graph_8KB, (0, 0))
    print("OK")
