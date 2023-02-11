[Easy]

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

**Input:** strs = ["flower","flow","flight"]
**Output:** "fl"

**Example 2:**

**Input:** strs = ["dog","racecar","car"]
**Output:** ""
**Explanation:** There is no common prefix among the input strings.

**Constraints:**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

Accepted

2.2M

Submissions

5.3M

---

![[Pasted image 20230211011043.png]]

This was the solution I quickly whipped up. but the assumption there that was proven wrong by the test cases was that each of the letters would be unique. ["aa","aa"] would fail for example. Instead, the best approach here, is to "merge" each result until you get the common prefix at the end. By merge, I mean taking each pair of strings and looking for the common prefix and taking that and applying it to the next string in the list.

After 15 min, my solution is the following

```
```python
def longestCommonPrefix(self, strs: List[str]) -> str:
      commonPrefix = ""

      def getCommonPrefix(left, right):
        if not left or not right:
          return ""
        x = 0
        while x < len(left) and x < len(right) and left[x] == right[x] :
          x += 1
        
        return left[0:x]

      def mergeWords(lastWord, words):
        if not words:
          return lastWord
        
        newPrefix = getCommonPrefix(lastWord, words[0])
        words.popleft()
        return mergeWords(newPrefix, words)
      
      if len(strs) == 1:
        return strs[0]

      return mergeWords(strs[0], deque(strs[1:]))
```

