class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tot = nums1 + nums2
        tot.sort()
        mid = len(tot)//2
        if len(tot) % 2:
            return tot[mid]
        else:
            return (tot[mid] + tot[mid-1])/2
