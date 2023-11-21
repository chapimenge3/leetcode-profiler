class Solution:
    def getMatch(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        i, j = 0, 0
        res = ""
        while i <= l1 - 1 and j <= l2 -1:
            if s1[i] != s2[j]:
                break

            res += s1[i]

            i += 1; j += 1

        return res

    def lcp(self, arr, low, high):
        if low == high:
            return arr[low]
        if high > low:
            mid = low + (high - low) // 2
            str1 = self.lcp(arr, low, mid)
            str2 = self.lcp(arr, mid+1, high)
            
            return self.getMatch(str1, str2)
            
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = self.lcp(strs, 0, len(strs) - 1)
        return res