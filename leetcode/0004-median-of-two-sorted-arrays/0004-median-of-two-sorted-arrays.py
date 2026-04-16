class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        i=0
        j=0
        while i<len(nums1) or j<len(nums2):
            if i<len(nums1) and j<len(nums2):
                if nums1[i]>nums2[j]:
                    arr.append(nums2[j])
                    j+=1
                else:
                    arr.append(nums1[i])
                    i+=1
            elif i<len(nums1):
                arr.extend(nums1[i:])
                break
            else:
                arr.extend(nums2[j:])
                break
        mid=len(arr)//2
        if len(arr)%2==0:
            
            return (arr[mid]+arr[mid-1])/2
        else:
            return arr[mid]
