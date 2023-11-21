class Solution {
public:
    int smallestRepunitDivByK(int k) {
        if(k % 2 == 0) return -1;

        int remainder = 1;
        set<int> prev_remainder;
        for(int i=1; i <= k; i++){
            int tmp = remainder % k; 
            if(tmp == 0) return i;
            int n = (remainder*10) + 1;
            remainder = n % k;
            if(prev_remainder.count(tmp)) return -1;
            prev_remainder.insert(tmp);
        }
        return -1;

    }
};