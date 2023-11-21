# Add Two Numbers

## Description

<p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>


Please see the [original problem description](https://leetcode.com/problems/add-two-numbers/).

## Stats

- **Runtime**: 115 ms
    - **Beats**: 5
- **Memory**: 14 MB
    - **Beats**: 100
- **Timestamp**: 16 August 2022

## Solution

You can find the solution [here](./add-two-numbers.py).

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        starter = None
        prev = None
        carry = 0
        while l1 or l2:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0 
            res_num = val_1 + val_2 + carry
            if res_num > 9:
                carry = 1
                res_num = res_num % 10
            else:
                carry = 0
            res_node = ListNode(val=res_num)
            if prev:
                prev.next = res_node
            
            prev = res_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not starter:
                starter = res_node
        
        if carry:
            node = ListNode(val=carry)
            prev.next = node

            
        return starter

```
