def inorder_traversal(root):
    """Performs an in-order traversal of a binary tree and returns the result as a list."""
    result = []

    def _inorder(node):
        if node:
            _inorder(node.left)
            result.append(node.val)
            _inorder(node.right)

    _inorder(root)
    return result