class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        d = {i for i in nums}
        nums_len = len(nums)
        _max = 2**nums_len
        for i in range(_max):
            bn = (bin(i)[2:]).zfill(nums_len)
            if bn not in d:
                return bn
            