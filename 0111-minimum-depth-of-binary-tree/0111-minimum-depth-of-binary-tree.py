# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        level=0
        if not root:
            return level
        while q:
            level+=1
            l=len(q)
            for i in range(l):
                val=q.popleft()
                if not val.left and not val.right:
                    return level
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
        