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

def longest_palindromic_substring(s):
    longest_palindrom = ''
    dp = [[0]*len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrom = s[i]

    for i in range(len(s)-1,-1,-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                if j-i ==1 or dp[i+1][j-1] is True:
                    dp[i][j] = True
                    if len(longest_palindrom) < j+1 - i :
                        longest_palindrom = s[i:j+1]
        # print_nested_array(dp)
    return longest_palindrom


print(longest_palindromic_substring("aabb") == "aa" or longest_palindromic_substring("aabb") == "bb")
print(longest_palindromic_substring("abab") == "aba" or longest_palindromic_substring("abab") == "bab")
print(longest_palindromic_substring("somethingg") == "gg")
print(longest_palindromic_substring("abba") == "abba")
print(longest_palindromic_substring("cac") == "cac")




