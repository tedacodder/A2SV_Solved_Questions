# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans=deque()
        answer=0
        
        def dfs(r):
            if not r:
                return
            if r.val%2==0 and (r.left or r.right):
                ans.append(r)
            dfs(r.left)
            dfs(r.right)  
        def grandparent(node):
            s=0
            if not node:
                return 0
            if node.left:
                s+=node.left.val
            if node.right:
                s+=node.right.val
            return s



        dfs(root)
        while ans:
            n=ans.pop()
            answer+=grandparent(n.left)+grandparent(n.right)
        
        return answer

