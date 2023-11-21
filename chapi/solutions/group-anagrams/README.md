# Group Anagrams

## Description

<p>Given an array of strings <code>strs</code>, group <strong>the anagrams</strong> together. You can return the answer in <strong>any order</strong>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/group-anagrams/).

## Stats

- **Runtime**: 109 ms
    - **Beats**: 28%
- **Memory**: 19.6 MB
    - **Beats**: 75%
- **Timestamp**: 03 July 2023

## Solution

You can find the solution [here](./group-anagrams.py).

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in range(len(strs)):
            sorted_i = ''.join(sorted(strs[i]))
            if sorted_i in anagrams:
                anagrams[sorted_i].append(strs[i])
            else:
                anagrams[sorted_i] = [strs[i]]
        
        return [anagrams[i] for i in anagrams]
        
        
        
```
