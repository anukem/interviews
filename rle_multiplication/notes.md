Multiply two RLE (Run-Length Encoded) arrays element-wise and produce resulting RLE array

Example if Run-Length Encoded Arrays:

[1, 1, 1, 2, 3, 3, 2, 2] => [(1, 3), (2, 1), (3, 2), (2, 2)]

Problem

Given two RLE arrays A and B, produce RLE array C, such that in non-RLE form each element C[i] is A[i] * B[i].

Example:

A = [(1, 3), (2, 1), (3, 2)] => [1, 1, 1, 2, 3, 3]

B = [(2, 3), (3, 3)] => [2, 2, 2, 3, 3, 3]

--------------------------------------------------

C = [(2, 3), (6, 1), (9, 2)] => [2, 2, 2, 6, 9, 9]

Example:

A = [(1, 3), (2, 1), (3, 2)] => [1, 1, 1, 2, 3, 3]

B = [(2, 3), (3, 4)] => [2, 2, 2, 3, 3, 3, 3]

--------------------------------------------------

C = [(2, 3), (6, 1), (9, 2), (0, 1)] => [2, 2, 2, 6, 9, 9, 0]

---

This was part 2 in a two part interview, but in general my thought process was to iterate through both arrays, while trying to maintain some state that helped me track whether or not I had fully processed a value at a given index in a or b. I start by taking the current value at index 0 and ask if I've reduced it down to 0 for the right hand side of the tuple. From there, once it hits 0, I would excise that element from the list and move onto the next one. If either list was empty before the other, I would just populate the resultant array with 0's going forward.

After about 20 minutes, the soltuion I came up with was

```
def multiply_rle(rle_a: List[Tuple[int,int]], rle_b: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    

    def condense(rle_a, rle_b, rle_c, index):

        if not rle_a:
            if rle_b:
                for i in range(len(rle_b)):
                    rle_c[index + i] = 0
            else:
                return rle_c
        else:
            if rle_a:
                for i in range(len(rle_a)):
                    rle_c[index + i] = 0
            else:
                return rle_c

        a, a_left = rle_a
        b, b_left = rle_b

        if a_left and b_left:
            rle_c[index] = a * b # <--- []
            a_left -= 1
            b_left -= 1
            if a_left == 0 and b_left == 0:
                return condense(rle_a[1:], rle_b[1:], rle_c, index + 1)
            elif a_left == 0 and b_left:
                return condense(rle_a[1:], rle_b, rle_c, index + 1)
            elif a_left and not b_left:
                return condense(rle_a, rle_b[1:], rle_c, index + 1)
            else:
                return condense(rle_a, rle_b, rle_c, index + 1)

    return condense(rle_a, rle_b, [], 0)
```

---

Spent some time looking at it afterwards since I wasn't able to get feedback on the final solution and found a couple bugs. After fixing those, my full soltuion was the following:

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

