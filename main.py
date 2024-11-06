class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self,u,v):
        if u not in self.adj_list:
            self.adj_list[u] = []

        if v not in self.adj_list:
            self.adj_list[v] = []
        
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, start, target, visited):
        #base case: where start node and the target node are same
        if start == target:
            return True
        
        visited.add(start)

        #explore all the neighbors of the start node

        for neighbor in self.adj_list[start]:
            if neighbor not in visited:
                if self.dfs(neighbor, target, visited):
                        return True

        return False #this is when no path is found
    
    def if_path_exists(self,start,target):
        if start not in self.adj_list or target not in self.adj_list: #check if both nodes exist in the graph
            return False
        
        visited = set() #keep a track of all visited nodes
        return self.dfs(start, target, visited)
    
#onobject of graph
graph = Graph()
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,3)
graph.add_edge(2,3)
graph.add_edge(3,4)

start_node = 0
target_node = 5

if graph.if_path_exists(start_node, target_node):
    print(f"The path exists between {start_node} and {target_node} .")
else:
    print("Sorry, no path was found.")