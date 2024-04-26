import heapq

def heuristic(node, goal):
    return 0  # Simple heuristic that always returns 0

def astar(graph, start, goal):
    priority_queue = []                # Priority queue to store nodes based on total cost
    heapq.heappush(priority_queue, (0, start))  # Push start node with cost 0
    came_from = {}                     # To keep track of the parent node for each node
    cost_so_far = {start: 0}           # Cost from start to each node

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            break  # Reached the goal node

        for neighbor in graph[current_node]:
            # Uniform cost of 1 for each step
            new_cost = cost_so_far[current_node] + 1

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current_node

    # Reconstruct the path from start to goal
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()  # Reverse to get the path from start to goal

    return path

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

    start_node = 'A'
    goal_node = 'F'

    # Find path using A* algorithm
    path = astar(graph, start_node, goal_node)
    print("A* Path from", start_node, "to", goal_node, ":", path)
