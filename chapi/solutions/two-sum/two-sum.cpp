class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int> > vi;
        int c = 0;
        for(auto i: nums){
            vi.push_back({i, c++});
        }
        sort(vi.begin(), vi.end());
        int i = 0, j = nums.size() - 1;
        while( i < j){
            int res = vi[i].first + vi[j].first;
            if (res == target){
                i = vi[i].second, j = vi[j].second;
                break;
            } else if(res < target){
                i++;
            } else {
                j--;
            }
        }
        return {i,j};
    }
};