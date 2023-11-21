class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> mp;
        vector<int> vi, tmp, small;
        if(nums1.size() > nums2.size()){
            tmp = nums1;
            small = nums2;
        }
        else {
            tmp = nums2;
            small = nums1;
        }
        for(auto i: tmp){
            mp[i]++;
        }
        for(auto i: small){
            if(mp[i] > 0){
                vi.push_back(i);
                mp[i]--;
            }
        }
        
        return vi;
    }
};