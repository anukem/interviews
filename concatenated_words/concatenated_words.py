
def print_2d_array(arr):
    for lst in arr:
        print(lst)

def concatenated_words(words):

    valid_words = set(words)
    def can_split_word(word):
        for idx in range(len(word)):
            left = word[:idx]
            right = word[idx:]

            if left in valid_words:
                if right in valid_words or can_split_word(right):
                    return True
        return False


    ans = []
    for word in words:
        if can_split_word(word):
            ans.append(word)
    return ans

print(concatenated_words(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]) == ["catsdogcats", "dogcatsdog", "ratcatdogcat"])
print(concatenated_words(["cat","cats", "catscats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]) == ["catscats", "catsdogcats", "dogcatsdog", "ratcatdogcat" ])
