class Direction:
  Up = 'Up'
  Down = 'down'
  Right = 'Right'
  Left = 'Left'

def canDescend(i, j, prevDirection, grid):
    if prevDirection == Direction.Right and grid[i][j] == -1:
      return False
    if prevDirection == Direction.Left and grid[i][j] == 1:
      return False

    return True


def descend(i, j, prevDirection, grid):
    if i < 0 or i > len(grid) or j < 0 or j >= len(grid[0]) or not canDescend(i, j, prevDirection, grid):
      return -1

    if i == len(grid) - 1 and (prevDirection == Direction.Left or prevDirection == Direction.Right ):
      return j

    nextDirection = Direction.Right if grid[i][j] == 1 else Direction.Left
    if prevDirection == Direction.Down:
      if nextDirection == Direction.Right:
        return descend(i, j + 1, nextDirection, grid)
      else:
        return descend(i, j - 1, nextDirection, grid)
    elif prevDirection == Direction.Right and nextDirection == Direction.Right:
        return descend(i + 1, j, Direction.Down, grid)
    elif prevDirection == Direction.Left and nextDirection == Direction.Left:
        return descend(i + 1, j, Direction.Down, grid)



grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]

assert [descend(0, x, Direction.Down, grid) for x in range(len(grid[0]))] == [1,-1,-1,-1,-1]
grid = [[-1]]
assert [descend(0, x, Direction.Down, grid) for x in range(len(grid[0]))] == [-1]

