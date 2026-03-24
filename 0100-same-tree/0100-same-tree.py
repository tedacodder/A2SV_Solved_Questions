# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1=deque([p])
        q2=deque([q])
        #side by side traversal
        while q1 and q2:
            length1=len(q1)
            length2=len(q2)
            s1=q1.pop()
            s2=q2.pop()
            if s1==None and s2==None:
                continue
            elif s1==None or s2==None:
                return False   
            elif  s1.val!=s2.val:
                return False
            q1.append(s1.left)
            q1.append(s1.right)
            q2.append(s2.left)
            q2.append(s2.right)
        return True

