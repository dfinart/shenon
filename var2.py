class Node:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability
        self.left = None
        self.right = None

def shannon_fano_tree(symbols):
    symbols = sorted(symbols, key=lambda x: x[1], reverse=True)
    if len(symbols) == 1:
        return Node(symbols[0][0], symbols[0][1])
    
    total_probability = sum(probability for symbol, probability in symbols)
    prefix_sum = 0
    optimal_index = 0
    for i, (symbol, probability) in enumerate(symbols):
        prefix_sum += probability
        if prefix_sum >= total_probability / 2:
            optimal_index = i
            break
    
    root = Node('', total_probability)
    root.left = shannon_fano_tree(symbols[:optimal_index+1])
    root.right = shannon_fano_tree(symbols[optimal_index+1:])
    
    return root

def print_tree(node, level=0, prefix=''):
    if node:
        print(' ' * (level*4) + prefix + str(node.symbol) + ' (' + str(node.probability) + ')')
        print_tree(node.left, level+1, 'L:')
        print_tree(node.right, level+1, 'R:')

symbols = [('S1', 0.02), ('S2', 0.11), ('S3', 0.12), ('S4', 0.01), ('S5', 0.09), ('S6', 0.15), ('S7', 0.08), ('S8', 0.13), ('S9', 0.04), ('S10', 0.14), ('S11', 0.06), ('S12', 0.05)]
root = shannon_fano_tree(symbols)
print_tree(root)

