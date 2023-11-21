class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        len_v1 = len(v1)
        len_v2 = len(v2)
        if len_v1 < len_v2:
            for i in range(len_v2):
                v1.append('0')
        elif len_v1 > len_v2:
            for i in range(len_v1):
                v2.append('0')
        
        for i, j in zip(v1, v2):
            if int(i) > int(j):
                return 1
            elif int(i) < int(j):
                return -1
            
        return 0

