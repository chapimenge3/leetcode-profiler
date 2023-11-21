# Minimum Number of Steps to Make Two Strings Anagram II

## Description

<p>You are given two strings <code>s</code> and <code>t</code>. In one step, you can append <strong>any character</strong> to either <code>s</code> or <code>t</code>.</p>

<p>Return <em>the minimum number of steps to make </em><code>s</code><em> and </em><code>t</code><em> <strong>anagrams</strong> of each other.</em></p>

<p>An <strong>anagram</strong> of a string is a string that contains the same characters with a different (or the same) ordering.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;<strong><u>lee</u></strong>tco<u><strong>de</strong></u>&quot;, t = &quot;co<u><strong>a</strong></u>t<u><strong>s</strong></u>&quot;
<strong>Output:</strong> 7
<strong>Explanation:</strong> 
- In 2 steps, we can append the letters in &quot;as&quot; onto s = &quot;leetcode&quot;, forming s = &quot;leetcode<strong><u>as</u></strong>&quot;.
- In 5 steps, we can append the letters in &quot;leede&quot; onto t = &quot;coats&quot;, forming t = &quot;coats<u><strong>leede</strong></u>&quot;.
&quot;leetcodeas&quot; and &quot;coatsleede&quot; are now anagrams of each other.
We used a total of 2 + 5 = 7 steps.
It can be shown that there is no way to make them anagrams of each other with less than 7 steps.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;night&quot;, t = &quot;thing&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> The given strings are already anagrams of each other. Thus, we do not need any further steps.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/).

## Stats

- **Runtime**: 761 ms
    - **Beats**: 5
- **Memory**: 29.1 MB
    - **Beats**: 97
- **Timestamp**: 13 November 2022

## Solution

You can find the solution [here](./minimum-number-of-steps-to-make-two-strings-anagram-ii.cpp).

```cpp
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
```
