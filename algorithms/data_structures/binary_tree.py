class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def in_order_traversal(self, node, visited=[]):
        if node:
            self.in_order_traversal(node.left, visited)
            visited.append(node.value)
            self.in_order_traversal(node.right, visited)
        return visited

    def pre_order_traversal(self, node, visited=[]):
        if node:
            visited.append(node.value)
            self.pre_order_traversal(node.left, visited)
            self.pre_order_traversal(node.right, visited)
        return visited

    def post_order_traversal(self, node, visited=[]):
        if node:
            self.post_order_traversal(node.left, visited)
            self.post_order_traversal(node.right, visited)
            visited.append(node.value)
        return visited

# Example usage:
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)

print("In-order Traversal:", tree.in_order_traversal(tree.root))
print("Pre-order Traversal:", tree.pre_order_traversal(tree.root))
print("Post-order Traversal:", tree.post_order_traversal(tree.root))