class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        l = [numbers[i] for i in s]
        llen = len(l)
        c = 0
        while c < llen:
            if c == llen-1:
                res += l[c]
            else:
                if l[c] < l[c+1]:
                    res += (l[c+1] - l[c])
                    c += 2
                    continue
                else:
                    res += l[c]
            c+=1
        return res