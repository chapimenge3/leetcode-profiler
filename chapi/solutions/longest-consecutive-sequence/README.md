# Longest Consecutive Sequence

## Description

<p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/longest-consecutive-sequence/).

## Stats

- **Runtime**: 1144 ms
    - **Beats**: 16%
- **Memory**: 70.9 MB
    - **Beats**: 27%
- **Timestamp**: 15 November 2023

## Solution

You can find the solution [here](./longest-consecutive-sequence.cpp).

```cpp
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
```
