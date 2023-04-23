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