class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [[nums[i], i] for i in range(len(nums))]
        new_nums.sort()
        last = len(nums) - 1
        first = 0
        while last > first:
            s = new_nums[first][0] + new_nums[last][0]
            if s == target:
                return [new_nums[first][1], new_nums[last][1]]
            elif s > target:
                last -= 1
            else:
                first += 1
            
            