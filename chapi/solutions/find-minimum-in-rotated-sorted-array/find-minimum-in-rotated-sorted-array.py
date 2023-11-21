class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])

        lef, rig = 0, len(nums)-1
        md = (lef+rig) // 2
        while lef < rig:
            md = (lef+rig)//2
            if nums[lef] > nums[md] < nums[rig]:
                rig = md
            elif nums[lef] < nums[md] > nums[rig]:
                lef = md
            
            elif nums[lef] < nums[md] < nums[rig]:
                rig = md
            
            if lef == rig-1:
                break

        return min(nums[lef], nums[rig], nums[md])


