[[Interview Question]]
You are given an array of strings `words`. Each element of `words` consists of **two** lowercase English letters.

Create the **longest possible palindrome** by selecting some elements from `words` and concatenating them in **any order**. Each element can be selected **at most once**.

Return _the **length** of the longest palindrome that you can create_. If it is impossible to create any palindrome, return `0`.

A **palindrome** is a string that reads the same forward and backward.

**Example 1:**

**Input:** words = ["lc","cl","gg"]
**Output:** 6
**Explanation:** One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

**Example 2:**

**Input:** words = ["ab","ty","yt","lc","cl","ab"]
**Output:** 8
**Explanation:** One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

**Example 3:**

**Input:** words = ["cc","ll","xx"]
**Output:** 2
**Explanation:** One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

**Constraints:**

-   `1 <= words.length <= 105`
-   `words[i].length == 2`
-   `words[i]` consists of lowercase English letters.


---
My thought process was to figure out some formula to generate to get the right result here. I knew that every non repeating pair had to have its reverse on the other side of any palindrome I wanted to create. I also knew that at the end of making those pairs, I could potentially add a repeating pair in the center to make it even longer. With both of those insights, here's what i got after 45 minutes. (i ended up having a bug in the way I was using the dictionary so I didn't solve this in time.)

```python
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

```



