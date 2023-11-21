class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = [[] for i in range(len(nums)+1)]
        p_storage = [0 for i in range(10**4)]
        n_storage = [0 for i in range(10**4)]

        for i in nums:
            if i >= 0:
                p_storage[i] += 1
            else:
                n_storage[-i] += 1
        
        for i in range(len(n_storage)):
            counter[n_storage[i]].append(-i)
        
        for i in range(len(p_storage)):
            counter[p_storage[i]].append(i)
        
        res = []
        for i in range(len(counter)-1, -1, -1):
            for j in counter[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
        return res

        
        
        
        

            

