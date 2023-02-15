# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Cardinality:
  Even = 'even'
  Odd = 'odd'

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
