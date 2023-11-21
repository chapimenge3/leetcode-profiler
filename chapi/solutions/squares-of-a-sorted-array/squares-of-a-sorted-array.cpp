class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> v;
        int i = 0, j = nums.size() - 1, sqi, sqj;
        while( i <= j ){
            sqi = nums[i] * nums[i];
            sqj = nums[j] * nums[j];
            if( sqi >= sqj ){
                v.push_back(sqi);
                i++;
            } else {
                v.push_back(sqj);
                j--;
            }
        }
        vector<int> vv(v.rbegin(), v.rend());
        return vv;
    }
};