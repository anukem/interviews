Given the `head` of a singly linked list, return `true` _if it is a_

_palindrome_

 _or_ `false` _otherwise_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

**Input:** head = [1,2,2,1]
**Output:** true

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)

**Input:** head = [1,2]
**Output:** false

**Constraints:**

- The number of nodes in the list is in the range `[1, 105]`.
- `0 <= Node.val <= 9`

**Follow up:** Could you do it in `O(n)` time and `O(1)` space?

---
Process is pretty straightforward. First iterate through the list and gather all of the values. At the end, return whether or not the list generated is equal to itself in reverse.

After about 10 minutes, here's the solution I came up with.

```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

      def traverse(head, palindrome):
        palindrome.append(head.val)
        if head.next == None:
          return palindrome == list(reversed(palindrome))
        
        return traverse(head.next, palindrome)
      
      return traverse(head, [])
```

