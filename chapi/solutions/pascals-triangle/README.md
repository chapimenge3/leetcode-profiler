# Pascal's Triangle

## Description

<p>Given an integer <code>numRows</code>, return the first numRows of <strong>Pascal&#39;s triangle</strong>.</p>

<p>In <strong>Pascal&#39;s triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> numRows = 5
<strong>Output:</strong> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> numRows = 1
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numRows &lt;= 30</code></li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/pascals-triangle/).

## Stats

- **Runtime**: 40 ms
    - **Beats**: 55%
- **Memory**: 14 MB
    - **Beats**: 100%
- **Timestamp**: 29 July 2022

## Solution

You can find the solution [here](./pascals-triangle.py).

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return l

        for i in range(3, numRows+1):
            tmp = []
            for j in range(i):
                if j == 0 or j == i-1:
                    tmp.append(1)
                else:
                    tmp.append(l[i-2][j-1] + l[i-2][j])
            l.append(tmp)
        return l
```
