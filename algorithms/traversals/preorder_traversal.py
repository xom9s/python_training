#recursive approach (classic)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node:
        print(node.data, end=" ")  # Visit (process) the node's data
        preorder_traversal(node.left)  # Traverse left subtree
        preorder_traversal(node.right)  # Traverse right subtree

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal:", end=" ")
preorder_traversal(root)  # Output: 1 2 4 5 3 

#iterative approach (using a stack)

def preorder_traversal_iterative(node):
    if node is None:
        return

    stack = [node]
    while stack:
        node = stack.pop()
        print(node.data, end=" ")

        if node.right:
            stack.append(node.right)  # Push right child first
        if node.left:
            stack.append(node.left)

# Example usage (same tree as above)
print("Iterative preorder traversal:", end=" ")
preorder_traversal_iterative(root)  # Output: 1 2 4 5 3