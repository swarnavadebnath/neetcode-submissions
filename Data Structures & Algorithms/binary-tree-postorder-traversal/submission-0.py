# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        s=[]
        curr = root
        while curr or s:
            if curr:
             res.append(curr.val)
             s.append(curr)
             curr = curr.right
            else:
             curr = s.pop()
             curr = curr.left
        res.reverse()
        return res
            

        