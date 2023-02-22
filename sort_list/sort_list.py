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

