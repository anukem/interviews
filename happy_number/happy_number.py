def isHappy(n: int) -> bool:
    seen = {}
    val = str(n)
    seen[val] = 1
    while val != "1" and seen[val] != 2:
        digits = [x for x in val]
        val = str(sum([int(x) ** 2 for x in digits]))

        if val not in seen:
            seen[val] = 1
        else:
            seen[val] += 1

    return val == "1"


assert isHappy(19) is True
assert isHappy(2) is False
