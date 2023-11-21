# Smallest Integer Divisible by K

## Description

<p>Given a positive integer <code>k</code>, you need to find the <strong>length</strong> of the <strong>smallest</strong> positive integer <code>n</code> such that <code>n</code> is divisible by <code>k</code>, and <code>n</code> only contains the digit <code>1</code>.</p>

<p>Return <em>the <strong>length</strong> of </em><code>n</code>. If there is no such <code>n</code>, return -1.</p>

<p><strong>Note:</strong> <code>n</code> may not fit in a 64-bit signed integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> k = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> The smallest answer is n = 1, which has length 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> k = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no such positive integer n divisible by 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The smallest answer is n = 111, which has length 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/smallest-integer-divisible-by-k/).

## Stats

- **Runtime**: 70 ms
    - **Beats**: 5
- **Memory**: 14.3 MB
    - **Beats**: 5
- **Timestamp**: 21 June 2023

## Solution

You can find the solution [here](./smallest-integer-divisible-by-k.cpp).

```cpp
class Solution {
public:
    int smallestRepunitDivByK(int k) {
        if(k % 2 == 0) return -1;

        int remainder = 1;
        set<int> prev_remainder;
        for(int i=1; i <= k; i++){
            int tmp = remainder % k; 
            if(tmp == 0) return i;
            int n = (remainder*10) + 1;
            remainder = n % k;
            if(prev_remainder.count(tmp)) return -1;
            prev_remainder.insert(tmp);
        }
        return -1;

    }
};
```
