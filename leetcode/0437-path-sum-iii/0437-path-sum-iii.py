# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixCount={0:1}
        def dfs(node,curr):
            if not node:
                return 0

            curr+=node.val
            count=prefixCount.get(curr-targetSum,0)
            prefixCount[curr]=prefixCount.get(curr,0)+1

            count+=dfs(node.left,curr)
            count+=dfs(node.right,curr)

            prefixCount[curr]-=1
            
            return count
        return dfs(root,0)

        