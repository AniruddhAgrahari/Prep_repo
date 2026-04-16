

class TreeNode:

    def __init__(self, val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inorder_traversal(self, root):
        
        if root is None:
            return 
        
        self.inorder_traversal(root.left)
        print(root.val)
        self.inorder_traversal(root.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
Solution().inorder_traversal(root)
