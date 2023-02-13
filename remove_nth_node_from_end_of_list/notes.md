Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

**Input:** head = [1,2,3,4,5], n = 2
**Output:** [1,2,3,5]

**Example 2:**

**Input:** head = [1], n = 1
**Output:** []

**Example 3:**

**Input:** head = [1,2], n = 1
**Output:** [1]

**Constraints:**

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

**Follow up:** Could you do this in one pass?

[[Linked List]]
---

Process here was relatively straightforward. I iterated through the list of values, maintaining a list of nodes that I'd seen, and when I get to the end, I check the value at n and remove it from the list, and return the head. The main issue I ran into was thinking about how to handle all the different edge cases that can come up. I.e what happens when there's only one element in the list. What happens when n is the length of the list etc etc.

After 47 min, the solution I came up with is as follows:

```
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      def traverse(node, collected):
        collected = collected + [node]
        if node.next == None:
          if len(collected) == 1:
            return None
          elif len(collected) == 2:
            if n == 1:
              collected[0].next = None
              return collected[0]
            else:
              return collected[1]
          else:
            if n == len(collected):
              return collected[1]
            nodeBeforeTheNodeToDrop = collected[len(collected) - n - 1]
            if n == 1:
              nodeBeforeTheNodeToDrop.next = None
              return collected[0]
            nodeBeforeTheNodeToDrop.next = collected[len(collected) - n + 1]
            
          return collected[0]
        
        return traverse(node.next, collected)
      
      return traverse(head, [])
```

Runtime is O(n) and the the space complexity is the same.
