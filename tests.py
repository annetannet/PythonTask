#!/usr/bin/env python3

import bfs
import dfs
import top_sort
import unittest


class TestGraphs(unittest.TestCase):
    def test_bfs_simple_graph(self):
        self.assertEqual(bfs.BFS([[1, 2], [0, 2], [0, 1, 3], [2]], 0), [0, 1, 2, 3])
        self.assertEqual(bfs.BFS([[1, 2, 3, 4, 5], [0], [0], [0], [0], [4]], 0), [0, 1, 2, 3, 4, 5])

    def test_bfs_directed_graph(self):
        self.assertEqual(bfs.BFS([[1, 2], [0, 2], [1]], 0), [0, 1, 2])
        self.assertEqual(bfs.BFS([[1, 2], [0, 2], [1]], 1), [1, 0, 2])
        self.assertEqual(bfs.BFS([[1, 2], [0, 2], [1]], 2), [2, 1, 0])

    def test_bfs_non_incident_nodes(self):
        self.assertEqual(bfs.BFS([[], [], [], []], 0), [0])
        self.assertEqual(bfs.BFS([[1, 2, 3], [], [], []], 1), [1])
        self.assertEqual(bfs.BFS([[1, 2, 3], [], [], []], 2), [2])
        self.assertEqual(bfs.BFS([[1, 2, 3], [1, 2, 3], [1, 2, 3], []], 3), [3])

    def test_bfs_empty_graph(self):
        self.assertEqual(bfs.BFS([], 0), [])
        self.assertEqual(bfs.BFS([], 1), [])
        self.assertEqual(bfs.BFS([], 2), [])

    def test_dfs_simple_graph(self):
        self.assertEqual(dfs.DFS([[1, 2], [3, 4], [], [], []], 0), [0, 1, 3, 4, 2])

    def test_dfs_common_graph(self):
        self.assertEqual(dfs.DFS(
            [[1, 2], [3, 4], [0, 1], [], [5, 6], [], [7, 8], [], []], 0),
            [0, 1, 3, 4, 5, 6, 7, 8, 2])

    def test_dfs_node_out_of_graph(self):
        self.assertEqual(dfs.DFS([[1, 2], [3, 4], [], [], []], 10), [])
        self.assertEqual(dfs.DFS([[1, 2], [3, 4], [1], [1]], 0), [0, 1, 3, 2])

    def test_dfs_no_repetition_visits(self):
        self.assertEqual(dfs.DFS([[1, 2], [3, 4], [1], [1], [0]], 0), [0, 1, 3, 4, 2])
        self.assertEqual(dfs.DFS([[1, 2], [3, 4], [0], [1], [1]], 0), [0, 1, 3, 4, 2])

    def test_topological_sort(self):
        self.assertEqual(top_sort.TopologicalSort([[1, 2], [3, 4], [3, 4], [5], [5], []]), [0, 2, 1, 4, 3, 5])


if __name__ == '__main__':
    unittest.main()
