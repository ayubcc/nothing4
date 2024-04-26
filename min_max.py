import math

def minimax(cur_depth, node_index, is_maximizing_player, scores, target_depth):
    if cur_depth == target_depth:
        return scores[node_index]

    if is_maximizing_player:
        max_eval = -math.inf
        for child_index in range(2):
            eval_value = minimax(cur_depth + 1, node_index * 2 + child_index, False, scores, target_depth)
            max_eval = max(max_eval, eval_value)
        return max_eval
    else:
        min_eval = math.inf
        for child_index in range(2):
            eval_value = minimax(cur_depth + 1, node_index * 2 + child_index, True, scores, target_depth)
            min_eval = min(min_eval, eval_value)
        return min_eval

def main():
    # Example game state initialization with user input
    num_nodes = int(input("Enter the number of nodes in the binary tree: "))
    scores = []

    print("Enter scores for each node (in level order, separated by spaces):")
    scores_input = input().split()
    
    if len(scores_input) != num_nodes:
        print("Invalid input! Number of scores does not match the number of nodes.")
        return

    for score in scores_input:
        try:
            scores.append(int(score))
        except ValueError:
            print("Invalid input! Please enter integer scores.")
            return
    
    tree_depth = math.log2(num_nodes)
    optimal_value = minimax(0, 0, True, scores, tree_depth)
    
    print("The optimal value at the root node is:", optimal_value)

if __name__ == "__main__":
    main()
