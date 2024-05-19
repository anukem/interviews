function expand_string(s: string): string {
  return s.split("").reduce(
    (
      acc: { currentNumber: string; currentString: string; stack: string[] },
      letter: string
    ) => {
      const { stack, currentNumber, currentString } = acc;

      if (letter === "[") {
        stack.push(currentString);
        stack.push(currentNumber);
        return {
          currentNumber: "",
          currentString: "",
          stack,
        };
      } else if (!isNaN(Number(letter))) {
        return { currentNumber: currentNumber + letter, currentString, stack };
      } else if (letter === "]") {
        const num = stack.pop();
        const prevStr = stack.pop();
        return {
          currentString: prevStr + currentString.repeat(Number(num)),
          stack,
          currentNumber,
        };
      } else {
        return { currentNumber, currentString: currentString + letter, stack };
      }
    },
    { currentNumber: "", currentString: "", stack: [] }
  ).currentString;
}

console.log(expand_string("3[a]d") === "aaad");
console.log(expand_string("3[a2[b]]d") === "abbabbabbd");
console.log(expand_string("10[a]d") === "aaaaaaaaaad");
