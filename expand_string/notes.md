You are given a string s containing encoded messages that need to be decoded. Each message is encoded using the following rules:

A digit n represents the number of times the subsequent string needs to be repeated.
A pair of brackets [] encloses the string that needs to be repeated n times.
Write a function decode_message(s: str) -> str that decodes the encoded messages in the input string s and returns the decoded string.

For example, given the input string "2[a]3[b]c", the function should return "aabbbbc", since "a" is repeated twice and "b" is repeated thrice.

Constraints:

The input string s contains only lowercase English letters, digits, and the characters '[' and ']'.
The input string s has length at most 10^4.
The input string s is well-formed and follows the encoding rules.


---

I spent 45 minutes going down a recursive solution route for this problem since I thought each
of the brackets were a sub problem, but after talking with chatgpt, while there is a recursive solution,
the iterative one using a stack was much more intuitive. The idea is to push onto the stack whenever
we encounter an open bracket, and to pop from the stack and calculate the current string with the last
number and string gathered after making a pass through the string.

