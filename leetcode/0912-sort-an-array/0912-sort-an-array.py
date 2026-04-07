class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(x,y):
            i=0
            j=0
            ans=[]
            while i<len(x) or j<len(y):
                if i>=len(x):
                    while j<len(y):
                        ans.append(y[j])
                        j+=1
                elif j>=len(y):
                    while i<len(x):
                        ans.append(x[i])
                        i+=1
                else:
                    if x[i]<y[j]:
                        ans.append(x[i])
                        i+=1
                    else:
                        ans.append(y[j])
                        j+=1
            return ans
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
        
            return merge(left_half, right_half)
        return mergeSort(0,len(nums)-1,nums)
