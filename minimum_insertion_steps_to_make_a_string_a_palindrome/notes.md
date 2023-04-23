[[Interview Question]]
[[Hard]]

Given a string `s`. In one step you can insert any character at any index of the string.

Return _the minimum number of steps_ to make `s` palindrome.

A **Palindrome String** is one that reads the same backward as well as forward.

**Example 1:**

**Input:** s = "zzazz"
**Output:** 0
**Explanation:** The string "zzazz" is already palindrome we do not need any insertions.

**Example 2:**

**Input:** s = "mbadm"
**Output:** 2
**Explanation:** String can be "mbdadbm" or "mdbabdm".

**Example 3:**

**Input:** s = "leetcode"
**Output:** 5
**Explanation:** Inserting 5 characters the string becomes "leetcodocteel".

**Constraints:**

-   `1 <= s.length <= 500`
-   `s` consists of lowercase English letters.

---

First attempt:

```python

class Step:
    Done = "Done"
    Added = "Added"
    Removed = "Removed"

def performStep(s):
    if s == s[::-1]:
        return s, Step.Done
    if len(s) == 1:
        return s, Step.Done
    elif len(s) == 2:
        if s[0] == s[1]:
            return s, Step.Done
        else:
            return s + s[0], Step.Added

    if s[0] == s[-1]:
        return s[1:len(s) - 1], Step.Removed
    else:
        return s + s[0], Step.Added


cur, step = performStep("zjveiiwvc")
total = 0
while True:
    if step == Step.Added:
        total += 1
    elif step == Step.Done:
        break
    cur, step = performStep(cur)
```

My thought was to keep appending to the end of the string or drop the two characters if they matched. That didn't work for the input "zjveiiwvc". 

Empirically trying to do that from first principles, it wasn't immediately clear to know how you know where to insert the character.

---
the solution:
### Overview

We are given a string `s`. We can step we can insert any character at any index of the string.

Our task is to return the minimum number of steps to make `s` palindrome.

---

### Approach 1: Recursive Dynamic Programming

#### Intuition

If you are new to Dynamic Programming, please see our [Leetcode Explore Card](https://leetcode.com/explore/featured/card/dynamic-programming/) for more information on it!

As our task is to insert minimum number of additional characters to `s` to make it a palindrome, we would want to figure out the longest palindromic subsequence that we can make from the characters in `s`. Characters that cannot be included in the longest palindromic subsequence must be adjusted by adding additional characters at required indices to form the entire string palindrome.

**The answer of the problem would be the length of `s` minus the length of the longest palindromic subsequence in `s`.**

```python
# find length of common subsequence
def lcs(s1, s2, memo):
    if not s1 or not s2:
        return 0
    
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    
    if s1[0] == s2[0]:
        memo[(s1, s2)] = 1 + lcs(s1[1:], s2[1:], memo);
        return memo[(s1, s2)]
    else:
        memo[(s1, s2)] = max(lcs(s1[1:], s2, memo), lcs(s1, s2[1:], memo))
        return memo[(s1, s2)]


def minimum_insertions(s):
    memo = {}
    return len(s) - lcs(s, s[::-1], memo)

print(minimum_insertions(s))
```

To find the length of the longest palindromic subsequence, we can compare the longest common subsequence of the string and its reverse since we know that anything left will need to have a character inserted to make things equal.

