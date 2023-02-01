Given an array of strings `words` (**without duplicates**), return _all the **concatenated words** in the given list of_ `words`.

A **concatenated word** is defined as a string that is comprised entirely of at least two shorter words in the given array.

**Example 1:**

**Input:** words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
**Output:** ["catsdogcats","dogcatsdog","ratcatdogcat"]
**Explanation:** "catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

**Example 2:**

**Input:** words = ["cat","dog","catdog"]
**Output:** ["catdog"]

---

Okay, so thinking about this in terms of [[dynamic programming]], my thought is to store a multi dimensional array where dp.(i)(j) == j when you remove all instances of i. so in the first example dp(0)(1) == s because when you remove "cat" from "cats", you're left with s.

At that point, if any element in the 2D array exists in the input words, we can be sure that it will be constructred by at least two words.


After 45 minutes, here's where I ended up:

```

def print_2d_array(arr):
    for lst in arr:
        print(lst)

def concatenated_words(words):
    reduced_words = [[("", True) for y in words] for x in words]
    ans = []
    valid_words = set(words)
    done = False
    while done != True:
        done = True
        for i in range(len(words)):
            for j in range(len(words)):
                replacement = words[j].replace(words[i], "")
                was_replaced = True if replacement != words[j] and replacement != '' else False


                if replacement == 'ratdog':
                    print(i, j)
                reduced_words[i][j] = (replacement, was_replaced)
                if replacement in valid_words and was_replaced:
                    ans.append(words[j])



    print_2d_array(reduced_words)
    print(ans)
    return ans

print(concatenated_words(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]) == ["catsdogcats", "dogcatsdog", "ratcatdogcat"])
```

This solution sort of works for cases where a word is comprised ONLY of two smaller words, but fails to grab the last word "ratdog" because its the result of first removing cat, and then removing rat and finally removing dog. The whole approach seemed like it could've worked, but looking at this after the fact, I think there's some data structure (A Trie?) that could've made life easier. In hindsight, if I was doing this again, i think I would try to use an algorithm to do DFS on a given word, using the existing dictionary, but not entirely sure that would work either.

