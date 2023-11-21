// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        // cout << n;
        long long left = 1, right = n, mid = (left + right) / 2, mint = 1, maxf ;
        bool badv;
        while (left <= right){
            badv = isBadVersion(mid);
            // cout << badv << " for " << mid << endl;
            if( badv ){
                right = mid - 1;
                mint = mid;
            }
            else {
                left = mid + 1;
            }
            mid = (left + right) / 2;
        }
        // cout << "The res is " << mint << endl;
        return int(mint) ;
        
    }
};