# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        dic={}
        q=deque([root])
        while q:
            value=q.popleft()
            if k-value.val in dic:
                return True
            dic[value.val]=dic.get(value.val,0)+1
            if value.left:
                q.append(value.left)
            if value.right:
                q.append(value.right)
        return False
