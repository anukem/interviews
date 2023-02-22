[[Interview Question]]
[Medium]
Given the `head` of a linked list, return _the list after sorting it in **ascending order**_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)

**Input:** head = [4,2,1,3]
**Output:** [1,2,3,4]

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)

**Input:** head = [-1,5,3,4,0]
**Output:** [-1,0,3,4,5]

**Example 3:**

**Input:** head = []
**Output:** []

---


```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

      if head == None:
        return None

      def gather_nodes(head, lst, idx):
        if head == None:
          return lst

        heappush(lst, (head.val,idx,head))
        return gather_nodes(head.next, lst, idx + 1)

      sorted_nodes = gather_nodes(head, [], 0)
      _, _, root = sorted_nodes[0]


      while sorted_nodes:
        _, _, current_node = heappop(sorted_nodes)
        if sorted_nodes:
          current_node.next = sorted_nodes[0][2]
        else:
          current_node.next = None

      return root

```
