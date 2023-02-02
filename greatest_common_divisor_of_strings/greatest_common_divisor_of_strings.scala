import scala.collection.mutable.ListBuffer

object Solution {

  def getMultiples(s: String): List[String] = {
    var multiples = ListBuffer[String]()
    for (i <- 1 to s.length) {
      if (s.length % i == 0 && (s.substring(0, i) * (s.length / i)) == s) {
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
    println(gcdOfStrings("ABCABC", "ABC"))
  }
}
