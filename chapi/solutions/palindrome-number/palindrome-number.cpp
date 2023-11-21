class Solution {
public:
    bool isPalindrome(int x) {
        long long num = x, revnum = 0, i;
        while(x > 0){
            i = x % 10;
            revnum *= 10;
            revnum += i;
            x /= 10;
        }
        return num == revnum;
    }
};