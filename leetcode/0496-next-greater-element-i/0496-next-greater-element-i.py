class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #we append the next greate element not the index not the number
        #stack
        answer={}
        for i in nums2:
            answer[i]=-1
        stack=[nums2[0]]
        i=1
        while stack and i<len(nums2):
            if stack[-1]<nums2[i]:
                while stack and stack[-1]<nums2[i]:
                    n=stack.pop()
                    answer[n]=nums2[i]
                
                stack.append(nums2[i])
                i+=1
            else:
                stack.append(nums2[i])
                i+=1
        print(stack)
        return [answer[i] for i in nums1]
        



        