# Longest Substring Without Repeating Characters

## Description

<p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without repeating characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/longest-substring-without-repeating-characters/).

## Stats

- **Runtime**: 34 ms
    - **Beats**: 17
- **Memory**: 8.6 MB
    - **Beats**: 82
- **Timestamp**: 10 November 2022

## Solution

You can find the solution [here](./longest-substring-without-repeating-characters.cpp).

```cpp
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
```
