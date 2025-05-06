import heapq
class Node:
    def _init_(self,name,g_cost,h_cost,parent=None):
        self.name = name
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = parent
    
    def f_cost(self):
        return self.g_cost + self.h_cost
    
    def _lt_(self,other):
        return self.f_cost() < other.f_cost()
    
graph = {}
heuristic = {}
    
def addEdge(from_node,to_node,cost):
    if from_node not in graph:
        graph[from_node] = []
    graph[from_node].append((to_node,cost))
    
def a_star_search(start,goal):
    openlist = []
    heapq.heappush(openlist,Node(start,0,heuristic[start]))
    closed_set=set()
        
    while openlist:
        current = heapq.heappop(openlist)
        if current.name == goal:
            print("Path Found:")
            print_path(current)
            print("\nTotal Cost:",current.g_cost)
            return
        closed_set.add(current.name)
            
        for neighbor_name,cost in graph.get(current.name,[]):
            if neighbor_name in closed_set:
                continue
            new_g_cost=current.g_cost + cost
            neighbor = Node(neighbor_name,new_g_cost,heuristic.get(neighbor_name,0),current)
            heapq.heappush(openlist,neighbor)
    print("path not found")
    
def print_path(node):
    if node.parent:
        print_path(node.parent)
    print(node.name,end='')
        
n = int(input("Enter the number of edges:"))
print("Enter the edges in format : from to cost")
for _ in range(n):
    u,v,cost = input().split()
    addEdge(u,v,int(cost))

m = int(input("Enter the numbers edges for heuristic:"))
print("Enter the value in format : node h_value")
for _ in range(m):
    node,h = input().split()
    heuristic[node] = int(h) 
    
start = input("Enter the starting point:")
goal = input("Enter the goal point:")

a_star_search(start,goal)