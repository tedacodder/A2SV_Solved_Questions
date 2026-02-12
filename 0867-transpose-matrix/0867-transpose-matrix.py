class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(matrix[0])):
            values=[]
            for j in range(len(matrix)):
                values.append(matrix[j][i])
            ans.append(values)
        return ans