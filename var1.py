class Node:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability
        self.bit = ""
        self.left = None
        self.right = None

def build_shannon_fano_tree(symbols, probabilities):
    nodes = [Node(symbols[i], probabilities[i]) for i in range(len(symbols))]
    nodes.sort(key=lambda x: x.probability, reverse=True)
    
    def split(nodes):
        total_prob = sum(node.probability for node in nodes)
        cumulative_prob = 0
        for i in range(len(nodes)):
            if cumulative_prob <= total_prob / 2 <= cumulative_prob + nodes[i].probability:
                return nodes[:i+1], nodes[i+1:]
            cumulative_prob += nodes[i].probability
    
    def build_tree(nodes):
        if len(nodes) == 1:
            return nodes[0]
        else:
            left, right = split(nodes)
            root = Node(None, sum(node.probability for node in nodes))
            root.left = build_tree(left)
            root.right = build_tree(right)
            return root
    
    return build_tree(nodes)

def assign_codes(node, code):
    if node is not None:
        node.bit = code
        assign_codes(node.left, code + "0")
        assign_codes(node.right, code + "1")

def print_codes(node):
    if node is not None:
        if node.symbol is not None:
            print(f"{node.symbol}: {node.bit}")
        print_codes(node.left)
        print_codes(node.right)

symbols = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12"]
probabilities = [0.02, 0.11, 0.12, 0.01, 0.09, 0.15, 0.08, 0.13, 0.04, 0.14, 0.06, 0.05]

root = build_shannon_fano_tree(symbols, probabilities)
assign_codes(root, "")
print_codes(root)
