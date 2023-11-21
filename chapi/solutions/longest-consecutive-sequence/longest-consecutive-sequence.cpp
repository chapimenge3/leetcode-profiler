class Solution {
  public: int longestConsecutive(vector < int > & nums) {
      if(nums.size() == 0) return 0;
      unordered_set<int> um;
      for(auto i: nums){
          um.insert(i);
      }

      int _max = 1, num, c = 1;
      for(auto i: nums) {
            c = 1;
            if(um.find(i- 1) == um.end()) { 
                num = i + 1;
                while(um.find(num) != um.end()) {
                    c++;
                    num++;
                }
            }
        _max = max(_max, c);
        }
      return _max;
  }
};