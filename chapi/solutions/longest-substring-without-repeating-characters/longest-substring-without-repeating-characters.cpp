class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int _max = 0, beg = 0, num = 0, i = 0;
        map<char, int> mp;
        std::map<char, int>::iterator it;

        for (auto c : s)
        {
            it = mp.find(c);
            if (it != mp.end() && it->second >= beg)
            {
                _max = max(_max, num);

                beg = it->second + 1;
                num = i - beg;
            }

            mp[c] = i;
            num += 1;
            i++;
        }

        return max(_max, num);
    }
};