from heapq import heappush, heappop
import unittest


def maxPerformance(n, speed, efficiency, k):
    cur_sum, h = 0, []
    ans = -float("inf")

    sorted_engineers = sorted(zip(efficiency, speed), reverse=True)
    for cur_eff, cur_speed in sorted_engineers:
        if len(h) > k - 1:
            cur_sum -= heappop(h)
        heappush(h, cur_speed)
        cur_sum += cur_speed
        ans = max(ans, cur_sum * cur_eff)

    return ans % (10**9 + 7)


class TestSamples(unittest.TestCase):
    def test_check_boolean(self):
        self.assertTrue(True)

    def test_compare_strings(self):
        self.assertEqual("abc", "abc")

    def test_compare_arrays(self):
        self.assertEqual([1, 2, 3], [1, 2, 3])

    def test_max_performance(self):
        test = maxPerformance(2, [2, 10, 4], [3, 4, 10], 2)
        self.assertEqual(test, 56)

    # def test_max_performance_with_k_as_three(self):
    #     test = maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3)
    #     self.assertEqual(test, 68)


unittest.main(exit=False)
