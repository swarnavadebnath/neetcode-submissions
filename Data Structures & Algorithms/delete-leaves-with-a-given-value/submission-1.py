# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node,t):
            if not node:
                return None
            node.left = dfs(node.left,t)
            node.right = dfs(node.right,t)
            if not node.right and not node.left and node.val == t:
                return None
            return node
        return dfs(root,target)