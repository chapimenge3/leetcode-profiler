class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        result.append(nums[-1])
        for i in range(n-2, -1, -1):
            pd = nums[i] * result[-1]
            result.append(pd)
        
        result = result[::-1]
        total = 1
        tmp = total
        for i in range(n):
            tmp = nums[i]
            # print(i, 'Result', result, 'Nums', nums, 'Total', total, end=' ')
            if i == 0:
                nums[i] = result[1]
            elif i == n-1:
                nums[i] = total
            else:
                nums[i] = total * result[i+1]
            total *= tmp
            # print()
        return nums

        





