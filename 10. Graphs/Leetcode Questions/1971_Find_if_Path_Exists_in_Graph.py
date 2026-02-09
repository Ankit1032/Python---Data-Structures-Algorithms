from collections import defaultdict
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # build adjacency list
        graph = defaultdict(list)
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS function
        def dfs(node):
            if node == destination:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)


# -----------------------------
# Test Driver
# -----------------------------
if __name__ == "__main__":

    n = 6
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2

    sol = Solution()
    result = sol.validPath(n, edges, source, destination)

    print(result)
