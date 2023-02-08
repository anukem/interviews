from typing import List


def totalFruit(self, fruits: List[int]) -> int:
    start, end = 0, 1

    if len(fruits) == 0:
        return 0
    elif len(fruits) == 1:
        return 1
    elif len(fruits) == 2:
        return 2

    maxLength = 2
    baskets = set([fruits[0], fruits[1]])
    while end < len(fruits):
        if fruits[end] in baskets:
            maxLength = max(maxLength, end - start + 1)
            end += 1
        elif len(baskets) == 2:
            start = end - 1
            while fruits[start] == fruits[end - 1]:
                start -= 1
                start += 1
                baskets = set([fruits[start], fruits[end]])
        else:
            baskets.add(fruits[end])
            maxLength = max(maxLength, end - start + 1)
