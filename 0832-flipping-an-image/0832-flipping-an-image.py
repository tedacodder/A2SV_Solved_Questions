class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in image:
            val=[]
            for j in i[::-1]:
                if j==0:
                    val.append(1)
                else:
                    val.append(0)
            ans.append(val)
        return ans
        

        