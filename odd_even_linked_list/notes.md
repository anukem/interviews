Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return _the reordered list_.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg)

**Input:** head = [1,2,3,4,5]
**Output:** [1,3,5,2,4]

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg)

**Input:** head = [2,1,3,5,6,4,7]
**Output:** [2,3,6,7,1,5,4]

**Constraints:**

- The number of nodes in the linked list is in the range `[0, 104]`.
- `-106 <= Node.val <= 106`

---
The thing that made this difficult was all the things you had to keep track of. You need a reference to the root of the odd and even starting points, so that you can connect them in the end, and you also need a reference to the current odd or even node and of course whichever node you're currently on. The last tricky part here was that I forgot to remove the reference to the next node so that when I connected them, I ended up with a cycle.

This ended up taking about an hour and a half which is way too long, but here's the result

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Cardinality:
  Even = 'even'
  Odd = 'odd'
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head:
        return None
      elif head.next == None:
        return head
      elif head.next.next == None:
        return head
      def traverse(oddRoot, evenRoot, cur, cardinality, currOdd, currEven):
        if cur is None:
          currOdd.next = evenRoot
          return oddRoot

        if oddRoot is None:
          oddRoot = cur
          currOdd = cur
        
        if cardinality == Cardinality.Odd:
          if not evenRoot:
            evenRoot = cur.next
            currEven = evenRoot
            nextNode = cur.next.next
            cur.next.next = None
            return traverse(oddRoot, evenRoot, nextNode, Cardinality.Odd, currOdd, currEven)

          currOdd.next = cur
          currOdd = cur
          nextNode = cur.next
          cur.next = None
          return traverse(oddRoot, evenRoot, nextNode, Cardinality.Even, currOdd, currEven)
        else:
          currEven.next = cur
          currEven = cur
          nextNode = cur.next
          cur.next = None
          return traverse(oddRoot, evenRoot, nextNode, Cardinality.Odd, currOdd, currEven)
      
      return traverse(None, None, head, Cardinality.Odd, None, None)
          
```

