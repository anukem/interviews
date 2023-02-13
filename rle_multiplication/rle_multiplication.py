def condense(rle_a, rle_b, rle_c, index):
    if not rle_a:
        if rle_b:
            for i in range(len(rle_b)):
                rle_c[index + i] = 0
        else:
            return rle_c
    elif not rle_b:
        if rle_a:
            for i in range(len(rle_a)):
                rle_c[index + i] = 0
        else:
            return rle_c

    a, a_left = rle_a[0]
    b, b_left = rle_b[0]

    if a_left and b_left:
        rle_c.append(a * b)  # <--- []
        a_left -= 1
        b_left -= 1
        rle_a[0] = (a, a_left)
        rle_b[0] = (b, b_left)
        if a_left == 0 and b_left == 0:
            return condense(rle_a[1:], rle_b[1:], rle_c, index + 1)
        elif a_left == 0 and b_left:
            return condense(rle_a[1:], rle_b, rle_c, index + 1)
        elif a_left and not b_left:
            return condense(rle_a, rle_b[1:], rle_c, index + 1)
        else:
            return condense(rle_a, rle_b, rle_c, index + 1)


assert condense([(1, 3), (2, 1), (3, 2)], [(2, 3), (3, 3)], [], 0) == [2, 2, 2, 6, 9, 9]
