# Permutation in String

## Description

<p>Given two strings <code>s1</code> and <code>s2</code>, return <code>true</code><em> if </em><code>s2</code><em> contains a permutation of </em><code>s1</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>In other words, return <code>true</code> if one of <code>s1</code>&#39;s permutations is the substring of <code>s2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidbaooo&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s2 contains one permutation of s1 (&quot;ba&quot;).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;ab&quot;, s2 = &quot;eidboaoo&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/permutation-in-string/).

## Stats

- **Runtime**: 51 ms
    - **Beats**: 98
- **Memory**: 13.9 MB
    - **Beats**: 100
- **Timestamp**: 12 January 2023

## Solution

You can find the solution [here](./permutation-in-string.py).

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_l = [0 for i in range(26)]
        s2_l = [0 for i in range(26)]
        s1l = len(s1)
        s2l = len(s2)
        for i in s1:
            s1_l[ord(i)-97] += 1
        
        for i in range(s1l):
            let = ord(s2[i])
            s2_l[let-97] += 1
        
        if s1_l == s2_l:
            return True
        
        for i in range(s1l, s2l):
            let = ord(s2[i])
            prev = ord(s2[i-s1l])
            s2_l[let-97] += 1
            s2_l[prev-97] -= 1

            if s1_l == s2_l:
                return True
        
        return False




```
