class Solution {
public:
    int minSteps(string s, string t) {
        map<char, int> sm, tm;

        for (auto i : s)
        {
            sm[i]++;
        }
        for (auto i : t)
        {
            tm[i]++;
        }
        int num = 0;
        std::map<char, int>::iterator it;
        for (auto i : sm)
        {
            it = tm.find(i.first);
            if (it != tm.end())
            {
                if (i.second > it->second)
                {
                    num += (i.second - it->second);
                }
            }
            else
            {
                num += i.second;
            }
        }

        for (auto i : tm)
        {
            it = sm.find(i.first);
            if (it != sm.end())
            {
                if (i.second > it->second)
                {
                    num += (i.second - it->second);
                }
            }
            else
            {
                num += i.second;
            }
        }

        return num;
    }
};