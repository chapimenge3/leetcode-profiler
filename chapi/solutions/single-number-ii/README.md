# Single Number II

## Description

<p>Given an integer array <code>nums</code> where&nbsp;every element appears <strong>three times</strong> except for one, which appears <strong>exactly once</strong>. <em>Find the single element and return it</em>.</p>

<p>You must&nbsp;implement a solution with a linear runtime complexity and use&nbsp;only constant&nbsp;extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,3,2]
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,1,0,1,99]
<strong>Output:</strong> 99
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li>Each element in <code>nums</code> appears exactly <strong>three times</strong> except for one element which appears <strong>once</strong>.</li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/single-number-ii/).

## Stats

- **Runtime**: 118 ms
    - **Beats**: 25%
- **Memory**: 16.1 MB
    - **Beats**: 100%
- **Timestamp**: 22 November 2022

## Solution

You can find the solution [here](./single-number-ii.py).

```python
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = Counter(nums)
        for i in n:
            if n[i] == 1:
                return i
```
