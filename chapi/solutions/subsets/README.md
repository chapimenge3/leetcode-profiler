# Subsets

## Description

<p>Given an integer array <code>nums</code> of <strong>unique</strong> elements, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span> <em>(the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the numbers of&nbsp;<code>nums</code> are <strong>unique</strong>.</li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/subsets/).

## Stats

- **Runtime**: 37 ms
    - **Beats**: 78
- **Memory**: 16.5 MB
    - **Beats**: 16
- **Timestamp**: 15 November 2023

## Solution

You can find the solution [here](./subsets.py).

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        for i in range(len(nums) + 1):
            subs.extend(map(list,itertools.combinations(nums, i)))
        
        return list(subs)
```
