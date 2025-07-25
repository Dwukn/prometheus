class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Adds an edge from node u to node v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def dfs(self, start):
        """Performs Depth-First Search (DFS) starting from 'start' node."""
        visited = set()
        self._dfs_helper(start, visited)

    def _dfs_helper(self, node, visited):
        """Helper method for DFS."""
        visited.add(node)
        print(node, end=" ")
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

    def bfs(self, start):
        """Performs Breadth-First Search (BFS) starting from 'start' node."""
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    g = Graph()

    # Add edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    # DFS traversal
    print("DFS traversal starting from node 0:")
    g.dfs(0)  # Output: 0 1 2 3 4

    print("\n")

    # BFS traversal
    print("BFS traversal starting from node 0:")
    g.bfs(0)  # Output: 0 1 2 3 4
