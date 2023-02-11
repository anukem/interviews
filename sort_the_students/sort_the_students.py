from typing import List
def sortTheStudents( score: List[List[int]], k: int) -> List[List[int]]:
      graded_sections = [(score[i][k], score[i]) for i in range(len(score))]
      graded_sections.sort()
      graded_sections.reverse()
      return [section[1] for section in graded_sections]

assert sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2) == [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
assert sortTheStudents([[3,4],[5,6]], 0) == [[5,6],[3,4]]

