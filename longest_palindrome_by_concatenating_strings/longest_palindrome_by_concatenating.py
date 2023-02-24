from collections import defaultdict
from typing import List
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
      seen = defaultdict(int)
      pairs = []

      for word in words:
        reversed_word = word[::-1]
        if reversed_word in seen:
          pairs.append((word, reversed_word))
          seen[reversed_word] -= 1
          if seen[reversed_word] == 0:
            del seen[reversed_word]
        else:
          seen[word] += 1

      extraPalindrome = False

      for key in seen:
        if seen[key] >= 1 and key == key[::-1]:
          extraPalindrome = True

      result = 2 if extraPalindrome else 0

      return len(pairs)*4 + result

assert Solution().longestPalindrome(['aa', 'aa']) == 4
assert Solution().longestPalindrome(['aa', 'aa', 'ab']) == 4
assert Solution().longestPalindrome(['aa', 'aa', 'ab', 'ba', 'cc']) == 10
