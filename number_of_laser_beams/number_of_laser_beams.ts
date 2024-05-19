function numberOfBeams(bank: string[]): number {
  function getLaserRelationShips(
    bank: string[],
    prevRow: string,
    totalRelationShips: number
  ): number {
    if (bank.length === 0) {
      return totalRelationShips;
    }

    const currentRow = bank[0];
    const bankRemaining = bank.slice(1);

    const currentOnes = currentRow
      .split("")
      .filter((letter) => letter === "1").length;
    const prevOnes = prevRow
      .split("")
      .filter((letter) => letter === "1").length;

    return getLaserRelationShips(
      bankRemaining,
      currentOnes >= 1 ? currentRow : prevRow,
      currentOnes >= 1
        ? currentOnes * prevOnes + totalRelationShips
        : totalRelationShips
    );
  }

  return getLaserRelationShips(bank, "", 0);
}

console.log(numberOfBeams(["011001", "000000", "010100", "001000"]));
console.log(numberOfBeams(["011001", "000000", "010100", "001000"])); // Output: 6
console.log(numberOfBeams(["111", "111", "111"])); // Output: 27
console.log(numberOfBeams(["000", "000", "000"])); // Output: 0
console.log(numberOfBeams(["101", "010", "101"])); // Output: 4