def dfs(graph, start):
    visited = set()            # To keep track of visited nodes
    stack = [start]            # Start DFS with the initial node
    traversal = []             # To store the traversal path

    while stack:
        node = stack.pop()     # Get the last node from the stack
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            traversal.append(node)

            # Add adjacent nodes to the stack
            # (We use reversed order to maintain the correct traversal order)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

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

# Starting DFS from node 'A'
result = dfs(graph, 'A')
print("DFS Traversal:", result)
