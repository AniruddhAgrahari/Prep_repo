# Base case: if node is None: return 0
# At each node: swap root.left and root.right
# Recursive case: invert left subtree, invert right subtree
# TC: O(n)
# SC: O(h)

class TreeNode:

    def __init__(self, val, left=None, right=None):
        
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def invert_binarytree(self, root):

        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invert_binarytree(root.left)
        self.invert_binarytree(root.right)
        return root
    

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
Solution().invert_binarytree(root)
assert root.left.val == 7
assert root.right.val == 2 

