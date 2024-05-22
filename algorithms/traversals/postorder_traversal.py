def printPostorder(root):
    if root:  # Base Case: If the current node exists (is not None)

        # 1. Traverse Left Subtree
        printPostorder(root.left) 

        # 2. Traverse Right Subtree
        printPostorder(root.right)

        # 3. Print Root
        print(root.val, end=" ") 