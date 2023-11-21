# Search Insert Position

## Description

<p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> contains <strong>distinct</strong> values sorted in <strong>ascending</strong> order.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/search-insert-position/).

## Stats

- **Runtime**: 4 ms
    - **Beats**: 29%
- **Memory**: 9.8 MB
    - **Beats**: 99%
- **Timestamp**: 14 March 2022

## Solution

You can find the solution [here](./search-insert-position.cpp).

```cpp
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        long long left = 0, right = nums.size() - 1, mid ;
        while(left <= right){
            mid = (left+ right) / 2 ;
            if(nums[mid] == target){
                return mid;
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        if(nums[mid] > target){
            return mid;
        }
        else {
            return mid + 1;
        }
    }
};
```
