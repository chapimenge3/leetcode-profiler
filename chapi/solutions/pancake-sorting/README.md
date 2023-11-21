# Pancake Sorting

## Description

<p>Given an array of integers <code>arr</code>, sort the array by performing a series of <strong>pancake flips</strong>.</p>

<p>In one pancake flip we do the following steps:</p>

<ul>
	<li>Choose an integer <code>k</code> where <code>1 &lt;= k &lt;= arr.length</code>.</li>
	<li>Reverse the sub-array <code>arr[0...k-1]</code> (<strong>0-indexed</strong>).</li>
</ul>

<p>For example, if <code>arr = [3,2,1,4]</code> and we performed a pancake flip choosing <code>k = 3</code>, we reverse the sub-array <code>[3,2,1]</code>, so <code>arr = [<u>1</u>,<u>2</u>,<u>3</u>,4]</code> after the pancake flip at <code>k = 3</code>.</p>

<p>Return <em>an array of the </em><code>k</code><em>-values corresponding to a sequence of pancake flips that sort </em><code>arr</code>. Any valid answer that sorts the array within <code>10 * arr.length</code> flips will be judged as correct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,2,4,1]
<strong>Output:</strong> [4,2,4,3]
<strong>Explanation: </strong>
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
After 1st flip (k = 4): arr = [<u>1</u>, <u>4</u>, <u>2</u>, <u>3</u>]
After 2nd flip (k = 2): arr = [<u>4</u>, <u>1</u>, 2, 3]
After 3rd flip (k = 4): arr = [<u>3</u>, <u>2</u>, <u>1</u>, <u>4</u>]
After 4th flip (k = 3): arr = [<u>1</u>, <u>2</u>, <u>3</u>, 4], which is sorted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3]
<strong>Output:</strong> []
<strong>Explanation: </strong>The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 100</code></li>
	<li><code>1 &lt;= arr[i] &lt;= arr.length</code></li>
	<li>All integers in <code>arr</code> are unique (i.e. <code>arr</code> is a permutation of the integers from <code>1</code> to <code>arr.length</code>).</li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/pancake-sorting/).

## Stats

- **Runtime**: 75 ms
    - **Beats**: 5%
- **Memory**: 14 MB
    - **Beats**: 100%
- **Timestamp**: 31 July 2022

## Solution

You can find the solution [here](./pancake-sorting.py).

```python
class Solution:

    def flip(self, arr, r, n):
        l = arr[:n]
        # print('L', l, r)
        ll = l[:r+1][::-1] + l[r+1:]
        rev = ll[::-1] + arr[n:]
        # print('Rev', rev)
        return rev 

            
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        l = sorted(arr)
        
        # if l == arr:
        #     return []
        
        res = []
        
        while n > 1:
            mx = max(arr[:n])
            ind = arr.index(mx)
            
            arr = self.flip(arr, ind, n)
            if ind:
                res.append(ind+1)
            
            res.append(n)
            n -= 1
            # print(f'Arr {arr} Max {mx} Res {res}')
        
        return res
        
        
```
