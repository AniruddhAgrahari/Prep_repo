#Base Case: If node is None, return 0
#Recursive Case: return 1 + max(left subtree depth, right subtree depth)

# TC: O(n) - visit every node once
# SC: O(h) - call stack depth equals tree height


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root):
    
        if root is None:
          return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
    


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
Solution().max_depth(root)
assert Solution().max_depth(root) == 3

root2 = TreeNode(1)
assert Solution().max_depth(root2) == 1

assert Solution().max_depth(None) == 0