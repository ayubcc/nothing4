from collections import deque

def dfs(graph, start):
    visited = set()            # To keep track of visited nodes
    stack = [start]            # Start DFS with the initial node
    traversal_dfs = []         # To store DFS traversal path

    while stack:
        node = stack.pop()     # Get the last node from the stack
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            traversal_dfs.append(node)

            # Add adjacent nodes to the stack
            # (We use reversed order to maintain the correct traversal order)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_dfs

def bfs(graph, start):
    visited = set()            # To keep track of visited nodes
    queue = deque([start])     # Start BFS with the initial node in a queue
    traversal_bfs = []         # To store BFS traversal path

    while queue:
        node = queue.popleft() # Get the first node from the queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            traversal_bfs.append(node)

            # Add adjacent nodes to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_bfs

# Example usage:
if __name__ == "__main__":
    # Define a graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Starting DFS from node 'A'
    result_dfs = dfs(graph, 'A')
    print("DFS Traversal:", result_dfs)

    # Starting BFS from node 'A'
    result_bfs = bfs(graph, 'A')
    print("BFS Traversal:", result_bfs)
