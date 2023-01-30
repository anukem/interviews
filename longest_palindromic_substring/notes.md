_Given a string `s`, return the longest palindromic substring_

"aabc" -> "aa"
"gafa" -> "afa"
"babad" -> "bab" | "aba"
"someaaaa" -> "aaaa"

My intiial thought was to start from the middle of the string, and keep going out until I find the largest substring that's a palindrome. The problem is that I might miss a long palindrome that falls somewhere randomly in the middle of the left or right hand side. My next thought was whether or not I could break down the problem into one that could be solved in pieces. I know that

1. A string of length 1 always has a longest palindrome substring of 1.
2. A string of length 2 either has a palindrome of length 2 or 1.
3. A string of length 3 has a palindrome of length 3, 2 or 1 etc.


So if I only had to solve it for strings of those lengths, I would return 1 for strings of length 1. For strings of length 2, I would check if they're both the same letter, and return either 1 or 2 depending on the result. For strings of length 3, I would check if the whole thing is a palindrome. If it is, i can return 3, otherwise, i'll look for a palindrome of length 2. If I don't find one, I can return 1.

To speed things up, I'll do a linear scan to check for the cardinality of each letter to help figure out the largest palindrome I can make.

So "aab" -> {a: 2, b: 1}

From here, I know that in order for the string consisting of the letters a, a, and b to contain a palindrome, one of two things needs to true. Either the two a's are on the outside of the palindrome (aba) or they're together (aab). In the first case, the whole string is trivially a palindrome because everything inbetween the two a's is a palindrome, so I can return aba since I was looking for a string of length 3. When they're together, all i can say is that's also a palindrome of length 2.

After 45 min, here's as far as I got.

```def longest_palindromic_substring(s):
    instances = {}
    for index, letter in enumerate(s):
        if letter not in instances:
            instances[letter] = [index]
        else:
            instances[letter].append(index)
    print(instances)


longest_palindromic_substring("aabb")
longest_palindromic_substring("abab")
longest_palindromic_substring("ababa")
longest_palindromic_substring("abba")

```



---------------------------------------------------------------------------------------------------------------

*the solution*

This one requires dynamic programming.So to build up a solution here, we first have to construct an array representing the slicing of the original string from i to j where dp.at(i).at(j) == s[i:j]


So for a word like "cac", it would be

|  c  |  ca  |  cac
|  ac |  a   |  ac
| cac |  ca  |  c

Next, we can cross out the bottom triange where i > j because it would require constructing the string backwards, which isn't possible.

That leaves us with

|  c  |  ca  |  cac
|     |  a   |  ac
|     |      |  c

Next, mark the table True across the diagonal
|  True  |       |
|        |  True |
|        |       |  True

i = 2
j = 3

*nothing happens*

i = 1
j = 2

s[i] = a
s[j] = c

*nothing happens because they're not equal*

i = 0
j = 1

s[i] = c
s[j] = a

*nothing happens because they're not equal*

i = 0
j = 2

s[i] = c
s[j] = c

j - i = 2 and dp.at(i+1)(j-1) = True

dp.at(0)(2)  = True

|  True  |       |  *True*
|        |  True |
|        |       |  True

longest_pal = s[0:2]

At the end, we can return longest_pal

After doing some research, it seems like there are two general approaches. You can either treat each letter in the string as the "center" of the longest palindrome, and expand out from there assuming that its either an odd length palindrome, or that its an even length palindrome, with the goal of finding out how far you can move two pointers while they're equal. OR you can use the DP approach above to basically build the same thing, but without the space complexity of having to splice the string each time.

Here's the "expand algo"

```

def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        right += 1
        left -= 1

    return s[left+1:right]

def my_longest_palindrome(s):
    palindromes_at_letter = []
    for index, letter in enumerate(s):
        even_palindrome = expand(s, index, index + 1) if index + 1 < len(s) and s[index] == s[index + 1] else ""
        odd_palindrome = expand(s, index, index)
        palindromes_at_letter.append(max([even_palindrome, odd_palindrome], key = len))

    return max(palindromes_at_letter, key = len)


```

