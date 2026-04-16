class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search():
            l=0
            r=len(matrix)-1
            while l<=r:
                mid=(l+r)//2
                if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                    return mid
                elif matrix[mid][0]>target:
                    r=mid-1
                else:
                    l=mid+1
            return -1
        def main():
            index=search()
            
            if index==-1:
                return False
            
            l=0
            r=len(matrix[index])-1

            while l<=r:
                mid=(l+r)//2
                if matrix[index][mid]==target:
                    return True
                elif matrix[index][mid]<target:
                    l=mid+1
                else:
                    r=mid-1
           
            return False
        return main()




        