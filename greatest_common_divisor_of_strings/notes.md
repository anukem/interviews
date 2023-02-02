[EASY]
For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + ... + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return _the largest string_ `x` _such that_ `x` _divides both_ `str1` _and_ `str2`.

**Example 1:**

**Input:** str1 = "ABCABC", str2 = "ABC"
**Output:** "ABC"

**Example 2:**

**Input:** str1 = "ABABAB", str2 = "ABAB"
**Output:** "AB"

**Example 3:**

**Input:** str1 = "LEET", str2 = "CODE"
**Output:** ""

---
Took the liberty of attempting this one in Scala since I eventually want to translate a majority of my programming in a language that supports static types and functional programming. Jury is still out on whether or not I make it my primary language for interviews. There were some guarantees I was hoping it would enforce that it didn't like static type checking, compile time errors that surface in the UI, etc. In any event, my approach here was to first find the deminators of each string, compare the result and take the largest string that fell in both sets.

```
import scala.collection.mutable.ListBuffer

  

object Solution {

def multiply(s: String, n: Int): String = {

val sb = new StringBuilder()

for (i <- 0 until n) {

sb.append(s)

}

sb.toString()

}

  

def getMultiples(s: String): List[String] = {

var multiples = ListBuffer[String]()

for (i <- 1 to s.length) {

if (s.length % i == 0 && multiply(s.substring(0, i), s.length / i) == s) {

multiples.insert(0, s.substring(0, i))

}

}

multiples.toList

}

  

def gcdOfStrings(str1: String, str2: String): String = {

val firstMultiples = getMultiples(str1)

val secondMultiple = getMultiples(str2).toSet

val gcd = ListBuffer[String]()

for (multiple <- firstMultiples) {

if (secondMultiple.contains(multiple)) {

gcd.addOne(multiple)

}

}

  

if (gcd.isEmpty) {

return ""

}

  

gcd.max

}

  

def main(args: Array[String]): Unit = {

gcdOfStrings("ABCABC", "ABC")

}

}
```

This passed all test cases and beat 87% of submissions.

