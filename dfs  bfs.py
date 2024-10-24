print("Joel Gonsalves 111")

graph = {
    'A': ['B', 'C'],
    'B': ['D','E'],
    'C': ['F'],
    'D':[],
    'E':['F'],
    'F':[]

    }

graph1 = { 'A' : ['B','C'],
 'B' : ['A','D','E'],
 'C' : ['A','F'],
 'D' : ['B'],
 'E' : ['B','F'],
 'F' : ['C','E']}

visited = []
queue = []

#BREADTH FIRST SEARCH#DEPTH FIRST SEARCH

def bfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        queue.append(node)

        while queue:
            m = queue.pop(0)
            print(m,end=" ")

            for neighbor in graph[m]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)


bfs(graph,'A',visited)



#DEPTH FIRST SEARCH

def dfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour , visited)
        return visited
dfs(graph1,'A',visited)
print(visited)
    







                    

