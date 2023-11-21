# Longest Common Prefix

## Description

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>Output:</strong> &quot;fl&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters.</li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/longest-common-prefix/).

## Stats

- **Runtime**: 85 ms
    - **Beats**: 5%
- **Memory**: 13.9 MB
    - **Beats**: 100%
- **Timestamp**: 15 July 2022

## Solution

You can find the solution [here](./longest-common-prefix.py).

```python
class Solution:
    def getMatch(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        i, j = 0, 0
        res = ""
        while i <= l1 - 1 and j <= l2 -1:
            if s1[i] != s2[j]:
                break

            res += s1[i]

            i += 1; j += 1

        return res

    def lcp(self, arr, low, high):
        if low == high:
            return arr[low]
        if high > low:
            mid = low + (high - low) // 2
            str1 = self.lcp(arr, low, mid)
            str2 = self.lcp(arr, mid+1, high)
            
            return self.getMatch(str1, str2)
            
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = self.lcp(strs, 0, len(strs) - 1)
        return res
```
