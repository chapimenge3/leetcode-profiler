class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        for i in range(len(nums) + 1):
            subs.extend(map(list,itertools.combinations(nums, i)))
        
        return list(subs)