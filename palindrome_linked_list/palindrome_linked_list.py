from typing import Optional
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def traverse(head, palindrome):
            palindrome.append(head.val)
            if head.next is None:
                return palindrome == list(reversed(palindrome))

            return traverse(head.next, palindrome)

        return traverse(head, [])


class TestSamples(unittest.TestCase):
    def test_check_boolean(self):
        self.assertTrue(True)

    def test_compare_strings(self):
        self.assertEqual("abc", "abc")

    def test_compare_arrays(self):
        self.assertEqual([1, 2, 3], [1, 2, 3])

    def test_is_palindrome(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(1)
        test = Solution().isPalindrome(head)
        self.assertEqual(test, True)


unittest.main(exit=False)
