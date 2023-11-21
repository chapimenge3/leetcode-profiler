class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        long long left = 0, right = nums.size() - 1, mid ;
        while(left <= right){
            mid = (left+ right) / 2 ;
            if(nums[mid] == target){
                return mid;
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        if(nums[mid] > target){
            return mid;
        }
        else {
            return mid + 1;
        }
    }
};