graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'

queue = [[start]]
visited = []

while queue:
    path = queue.pop(0)
    node = path[-1]
    
    if node not in visited:
        print('visited ',node)
        visited.append(node)
        
    if node == goal:
        print('path is',path)
        break
    
    for neighbour in graph[node]:
        new_path = path + [neighbour]
        queue.append(new_path)