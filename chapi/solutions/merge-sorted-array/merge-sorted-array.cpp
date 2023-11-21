class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> vi;
        int i = 0, j = 0;
        for(int k=0; k< n + m; k++){
            if(i >= m ) {
                vi.push_back(nums2[j]);
                j++;
            } else if ( j >= n) {
                vi.push_back(nums1[i]);
                i++;
            } else if ( nums1[i] <= nums2[j] ) {
                vi.push_back(nums1[i]);
                i++;
            } else {
                vi.push_back(nums2[j]);
                j++;
            }
        }
        nums1 = vi;
    }
};