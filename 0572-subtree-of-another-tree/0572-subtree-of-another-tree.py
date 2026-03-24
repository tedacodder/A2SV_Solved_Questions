# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def bfs(s,sub):
            q1=deque([s])
            q2=deque([sub])
            #side by side traversal
            while q1 and q2:
                length1=len(q1)
                length2=len(q2)
                s1=q1.popleft()
                s2=q2.popleft()
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
            return not q1 and not q2
        start=None
        r=root
        q=deque([r])
        possible=[]
        while q :
            value=q.popleft()
            if value.val==subRoot.val:
                possible.append(value)
            if value.left:
                q.append(value.left)
            if value.right:
                q.append(value.right)
        if possible:
            for p in possible:
                if bfs(p,subRoot):
                    return True
            
        return False
        