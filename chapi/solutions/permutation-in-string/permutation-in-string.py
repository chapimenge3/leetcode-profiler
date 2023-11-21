class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_l = [0 for i in range(26)]
        s2_l = [0 for i in range(26)]
        s1l = len(s1)
        s2l = len(s2)
        for i in s1:
            s1_l[ord(i)-97] += 1
        
        for i in range(s1l):
            let = ord(s2[i])
            s2_l[let-97] += 1
        
        if s1_l == s2_l:
            return True
        
        for i in range(s1l, s2l):
            let = ord(s2[i])
            prev = ord(s2[i-s1l])
            s2_l[let-97] += 1
            s2_l[prev-97] -= 1

            if s1_l == s2_l:
                return True
        
        return False



