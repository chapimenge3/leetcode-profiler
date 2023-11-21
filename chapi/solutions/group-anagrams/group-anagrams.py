class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(len(strs)):
            sorted_i = ''.join(sorted(strs[i]))
            if sorted_i in anagrams:
                anagrams[sorted_i].append(strs[i])
            else:
                anagrams[sorted_i] = [strs[i]]
        
        return [anagrams[i] for i in anagrams]
        
        
        