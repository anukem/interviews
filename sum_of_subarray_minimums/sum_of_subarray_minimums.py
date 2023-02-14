def sum_of_subarray_minimums(arr):
    stack = [(-1, -1)]
    A = [0 for x in arr]
    arr.append(0)

    for i, elem in enumerate(arr):
        while stack and elem < stack[-1][1]:
            checkedIndex, checkedValue = stack.pop()
            distanceToLesserValueOnLeft = checkedIndex - stack[-1][0]
            distanceToLesserValueOnRight = i - checkedIndex
            A[checkedIndex] = (
                checkedValue
                * distanceToLesserValueOnLeft
                * distanceToLesserValueOnRight
            )

        stack.append((i, elem))

    return sum(A) % (10**9 + 7)


print(sum_of_subarray_minimums([3, 1, 2, 4]))