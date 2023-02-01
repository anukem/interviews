_A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

-   For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

-   For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.
-   Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.
-   While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, _find the next permutation of_ `nums`.

The replacement must be **[in place](http://en.wikipedia.org/wiki/In-place_algorithm)** and use only constant extra memory._

---
My thought process here is to figure out how to handle incrementing the number I was given. I _think_ that to get to the next highest number, assuming the last digit is greater than the one right before, I can swap the last two digits and ensure that its at least greater than its predecessor.

So in the case of [1, 2, 3] -> [1, 3, 2] works. and so does [2, 1, 3] -> [2, 3, 1]. In fact, I think this works for any i j where i < j and nums[i] < nums[j]. So I need to first identify where I can make the swap, and if I can't do it anywhere, return the array sorted from smallest to largest.

After 45 min,

```
def next_permutation(arr):



print(next_permutation([1,2,3]) == [1,3,2])
print(next_permutation([1,3,2]) == [2,1,3])
print(next_permutation([3,1,2]) == [1,2,3])

```

I spent a bunch of time thinking about how to convert a given permutation to some representation that would show where it was in the total list, so that i could augment that number and then convert back to get the answer.


1 [1,2,3]
2 [1,3,2]
3 [2,1,3]
4 [2,3,1]
5 [3,1,2]
6 [3,2,1]

Something like [1,3,2] -> (2 + 1) % 6 = 3 -> [2,1,3]

I tried converting them to base 9, base 6, and base 3 to look for patterns, and found nothing.
I tried to look at the differences between each number to see if there was some ascending pattern and found nothing.

---

*the solution*

#### Generation in lexicographic order[[edit](https://en.wikipedia.org/w/index.php?title=Permutation&action=edit&section=29 "Edit section: Generation in lexicographic order")]

There are many ways to systematically generate all permutations of a given sequence.[[48]](https://en.wikipedia.org/wiki/Permutation#cite_note-sedegewick1977-53) One classic, simple, and flexible algorithm is based upon finding the next permutation in [lexicographic ordering](https://en.wikipedia.org/wiki/Lexicographic_ordering "Lexicographic ordering"), if it exists. It can handle repeated values, for which case it generates each distinct multiset permutation once. Even for ordinary permutations it is significantly more efficient than generating values for the Lehmer code in lexicographic order (possibly using the [factorial number system](https://en.wikipedia.org/wiki/Factorial_number_system "Factorial number system")) and converting those to permutations. It begins by sorting the sequence in (weakly) [increasing](https://en.wikipedia.org/wiki/Increasing "Increasing") order (which gives its lexicographically minimal permutation), and then repeats advancing to the next permutation as long as one is found. The method goes back to [Narayana Pandita](https://en.wikipedia.org/wiki/Narayana_Pandit "Narayana Pandit") in 14th century India, and has been rediscovered frequently.[[49]](https://en.wikipedia.org/wiki/Permutation#cite_note-FOOTNOTEKnuth20051%E2%80%9326-54)

The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place.

1.  Find the largest index _k_ such that _a_[_k_] < _a_[_k_ + 1]. If no such index exists, the permutation is the last permutation.
2.  Find the largest index _l_ greater than _k_ such that _a_[_k_] < _a_[_l_].
3.  Swap the value of _a_[_k_] with that of _a_[_l_].
4.  Reverse the sequence from _a_[_k_ + 1] up to and including the final element _a_[_n_].

For example, given the sequence [1, 2, 3, 4] (which is in increasing order), and given that the index is [zero-based](https://en.wikipedia.org/wiki/Zero-based_numbering "Zero-based numbering"), the steps are as follows:

1.  Index _k_ = 2, because 3 is placed at an index that satisfies condition of being the largest index that is still less than _a_[_k_ + 1] which is 4.
2.  Index _l_ = 3, because 4 is the only value in the sequence that is greater than 3 in order to satisfy the condition _a_[_k_] < _a_[_l_].
3.  The values of _a_[2] and _a_[3] are swapped to form the new sequence [1, 2, 4, 3].
4.  The sequence after _k_-index _a_[2] to the final element is reversed. Because only one value lies after this index (the 3), the sequence remains unchanged in this instance. Thus the lexicographic successor of the initial state is permuted: [1, 2, 4, 3].

Following this algorithm, the next lexicographic permutation will be [1, 3, 2, 4], and the 24th permutation will be [4, 3, 2, 1] at which point _a_[_k_] < _a_[_k_ + 1] does not exist, indicating that this is the last permutation.

This method uses about 3 comparisons and 1.5 swaps per permutation, amortized over the whole sequence, not counting the initial sort.[[50]](https://en.wikipedia.org/wiki/Permutation#cite_note-55)

```

def is_descending(arr):
    elements = [10]
    for idx, item in enumerate(arr):
        if elements[idx] < item:
            return False

        elements.append(item)
    return True


def get_low_swap(arr):
    i = len(arr) - 2
    while i > -1:
        if arr[i] < arr[i+1]:
            return i
        i = i - 1

def get_highest_index_greater_than_low_swap(arr, low_swap):
    i = len(arr) - 1
    while i > low_swap:
        if arr[i] > arr[low_swap]:
            return i
        i = i - 1

def swap(low, high, arr):
    newArr = arr.copy()
    newArr[low] = arr[high]
    newArr[high] = arr[low]
    return newArr

def next_permutation(arr):
    if is_descending(arr):
        arr.reverse()
        return arr

    # find the first case where arr[i] < arr[i+1]
    low_swap = get_low_swap(arr)
    high_swap = get_highest_index_greater_than_low_swap(arr, low_swap)

    arr = swap(low_swap, high_swap, arr)

    # reverse the rest of the list
    part_to_reverse = arr[low_swap+1:]
    part_to_reverse.reverse()

    return arr[:low_swap + 1] + part_to_reverse


print(next_permutation([1,2,3]) == [1,3,2])
print(next_permutation([1,3,2]) == [2,1,3])
print(next_permutation([3,1,2]) == [3,2,1])
print(next_permutation([3,2,1]) == [1,2,3])

```

