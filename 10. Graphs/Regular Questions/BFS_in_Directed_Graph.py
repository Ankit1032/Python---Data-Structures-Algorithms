#link: https://www.geeksforgeeks.org/python/python-program-for-breadth-first-search-or-bfs-for-a-graph/

from collections import defaultdict

#Directed Graph
class Graph:

    def __init__(self):
        
        #default dictionary to store graph
        self.graph = defaultdict(list)

    #Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    #Function to print BFS
    def BFS(self, u):
        
        #Mark all the vertices as not visited
        visited = [False] * len(self.graph.keys())

        #Create a queue for BFS
        queue = []

        #Mark the source code as visited and enqueue it
        queue.append(u)
        visited[u] = True

        while queue:
            
            node = queue.pop(0)
            print(node, end=' | ')

            for v in self.graph[node]:
                if visited[v] == False:
                    queue.append(v)
                    visited[v] = True


# Driver code
if __name__ == '__main__':

    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
        " (starting from vertex 2)")
    g.BFS(2)
    



