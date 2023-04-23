function getHappyString(n: number, k: number): string {
  const possibleLetters = ["a", "b", "c"];
  function getAllHappyStrings(
    n: number,
    strs: string[],
    previousLetter: string
  ): string[] {
    if (n == 0) {
      return strs;
    }
    const allStrings: string[][] = [];
    const unusedLetters = possibleLetters.filter(
      (letter) => letter !== previousLetter
    );

    for (const letter of unusedLetters) {
      allStrings.push(
        getAllHappyStrings(
          n - 1,
          strs.map((str) => {
            return str.concat(letter);
          }),
          letter
        )
      );
    }

    return allStrings.flat();
  }

  const options = getAllHappyStrings(n, [""], "");
  return k - 1 >= options.length ? "" : options[k - 1];
}
