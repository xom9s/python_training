class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def dfs(self):  
        """Depth-first traversal starting from the current node."""
        result = []
        stack = [self]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)  # Push right child first
            if node.left:
                stack.append(node.left)   # Push left child last
        return result