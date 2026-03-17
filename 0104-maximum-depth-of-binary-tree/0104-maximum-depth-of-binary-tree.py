# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        count=0
        if not root:
            return 0
        while q:
            count+=1
            length=len(q)
            for _ in range(length):
                value=q.popleft()
                if value.left:
                    q.append(value.left)
                if value.right:
                    q.append(value.right)
        return count
