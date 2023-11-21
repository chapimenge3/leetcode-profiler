# Valid Parentheses

## Description

<p>Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
	<li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()[]{}&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(]&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>&#39;()[]{}&#39;</code>.</li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/valid-parentheses/).

## Stats

- **Runtime**: 46 ms
    - **Beats**: 11
- **Memory**: 13.9 MB
    - **Beats**: 100
- **Timestamp**: 18 July 2022

## Solution

You can find the solution [here](./valid-parentheses.py).

```python
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if len(l) == 0:
                l.append(i)
            elif i == ')' and l[-1] == '(':
                l.pop()
            elif i == ']' and l[-1] == '[':
                l.pop()
            elif i == '}' and l[-1] == '{':
                l.pop()
            else:
                l.append(i)
        
        return len(l) == 0

        
```
