# Search a 2D Matrix

## Description

<p>You are given an <code>m x n</code> integer matrix <code>matrix</code> with the following two properties:</p>

<ul>
	<li>Each row is sorted in non-decreasing order.</li>
	<li>The first integer of each row is greater than the last integer of the previous row.</li>
</ul>

<p>Given an integer <code>target</code>, return <code>true</code> <em>if</em> <code>target</code> <em>is in</em> <code>matrix</code> <em>or</em> <code>false</code> <em>otherwise</em>.</p>

<p>You must write a solution in <code>O(log(m * n))</code> time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>-10<sup>4</sup> &lt;= matrix[i][j], target &lt;= 10<sup>4</sup></code></li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/search-a-2d-matrix/).

## Stats

- **Runtime**: 50 ms
    - **Beats**: 54%
- **Memory**: 14.4 MB
    - **Beats**: 100%
- **Timestamp**: 29 July 2022

## Solution

You can find the solution [here](./search-a-2d-matrix.py).

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        m = (l+r) // 2
        
        while l < r:
            m = (l+r) // 2
            key = matrix[m][0]
            if key == target:
                return True
            mlind, mlval = None, None
            if 0 <= m - 1 < len(matrix):
                mlind, mlval = m -1, matrix[m - 1][0]
            
            mrind, mrval = None, None
            if 0 <= m + 1 < len(matrix):
                mrind, mrval = m + 1, matrix[m + 1][0]
            
            if mlind is not None and ((mlval <= target < matrix[m][0])):
                m = mlind
                break
            
            if m < len(matrix) and ((matrix[m][0] <= target < mrval)):
                break
            
            if target < key:
                r = m - 1
            else:
                l = m + 1

        l = m - 1
        r = m + 1
        row = []
        # print(l,m,r, len(matrix))
        if l >= 0 and (matrix[l][0] <= target < matrix[m][0]):
            row = matrix[l]
        elif r < len(matrix) and matrix[m][0] <= target < matrix[r][0] :
            row = matrix[m]
        else:
            if r >= len(matrix):
                row = matrix[-1]
            else:
                row = matrix[r]
        
        l = 0
        r = len(row) - 1
        m = (l+r) // 2
        # print('Row', row)
        while l <= r:
            m = (l+r) // 2
            key = row[m]
            if key == target:
                return True
            elif target < key:
                r = m - 1
            else:
                l = m + 1

        return False
```
