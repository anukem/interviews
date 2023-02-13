from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class TestSamples(unittest.TestCase):
    def test_check_boolean(self):
        self.assertTrue(True)

    def test_compare_strings(self):
        self.assertEqual("abc", "abc")

    def test_compare_arrays(self):
        self.assertEqual([1, 2, 3], [1, 2, 3])

    def test_remove_nth_item(self):
        head = ListNode()
        head.next = ListNode()
        head.next.next = ListNode()
        head.next.next.next = ListNode()
        head.next.next.next.next = ListNode()
        test = Solution().removeNthFromEnd(head, 1)
        self.assertEqual(test, head)

    # def test_max_performance_with_k_as_three(self):
    #     test = maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3)
    #     self.assertEqual(test, 68)


unittest.main(exit=False)
