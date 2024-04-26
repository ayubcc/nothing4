from collections import deque

def bfs(graph, start):
    visited = set()            # To keep track of visited nodes
    queue = deque([start])     # Start BFS with the initial node in a queue
    traversal = []             # To store the traversal path

    while queue:
        node = queue.popleft() # Get the first node from the queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            traversal.append(node)

            # Add adjacent nodes to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal

# Example usage:
# Define a graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting BFS from node 'A'
result = bfs(graph, 'A')
print("BFS Traversal:", result)
