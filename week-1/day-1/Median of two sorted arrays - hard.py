class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArr = [0]*(len(nums1)+len(nums2))
        l=0
        r=0
        k=0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                mergedArr[k] = nums1[l]
                l+=1
            else:
                mergedArr[k] = nums2[r]
                r+=1
            k+=1
        
        while l < len(nums1):
            mergedArr[k] = nums1[l]
            l+=1
            k+=1

        while r < len(nums2):
            mergedArr[k] = nums2[r]
            r+=1
            k+=1
        
        length = len(mergedArr)//2
        if len(mergedArr)%2 == 0:
            return (mergedArr[length-1]+mergedArr[length])/2
        else:
            return mergedArr[length]
