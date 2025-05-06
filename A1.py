from collections import deque

class Graph:
    def _init_(self):
        self.graph = {}

    def addEdges(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, queue, visited):
        if not queue:
            return
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        self.bfs(queue, visited)

    def bfs_recursive(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        self.bfs(queue, visited)

def menu():
    g = Graph()
    while True:
        print("---Menu---\n1. Add Edges\n2. DFS\n3. BFS\n4. Exit")
        optn = input("Enter your choice: ")
        if optn == '1':
            u = int(input("Enter the vertex (u): "))
            v = int(input("Enter the vertex (v): "))
            g.addEdges(u, v)
        elif optn == '2':
            start = int(input("Enter the starting point: "))
            print("DFS:")
            g.dfs(start)
            print()
        elif optn == '3':
            start = int(input("Enter the starting point: "))
            print("BFS:")
            g.bfs_recursive(start)
            print()
        elif optn == '4':
            break
        else:
            print("Enter valid option")

if __name__ == "__main__":
    menu()