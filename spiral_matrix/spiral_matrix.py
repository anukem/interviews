class Direction:
    Up = "Up"
    Down = "down"
    Right = "right"
    Left = "left"


def directionalUpdate(i, j, direction):
    if direction == Direction.Up:
        return (i - 1, j)
    if direction == Direction.Right:
        return (i, j + 1)
    if direction == Direction.Down:
        return (i + 1, j)
    if direction == Direction.Left:
        return (i, j - 1)


def rotate(direction):
    if direction == Direction.Up:
        return Direction.Right
    if direction == Direction.Right:
        return Direction.Down
    if direction == Direction.Down:
        return Direction.Left
    if direction == Direction.Left:
        return Direction.Up


def canGoInDirection(direction, i, j, collected):
    if direction == Direction.Left and j - 1 >= 0 and (i, j - 1) not in collected:
        return True
    elif direction == Direction.Up and i - 1 >= 0 and (i - 1, j) not in collected:
        return True
    elif (
        direction == Direction.Right
        and j + 1 < len(matrix[0])
        and (i, j + 1) not in collected
    ):
        return True
    elif (
        direction == Direction.Down
        and i + 1 < len(matrix)
        and (i + 1, j) not in collected
    ):
        return True

    return False


def descend(matrix, i, j, collected, order, prevDirection):
    if len(collected) == len(matrix) * len(matrix[0]):
        return order

    if canGoInDirection(prevDirection, i, j, collected):
        collected.add((i, j))
        if prevDirection == Direction.Up:
            return descend(
                matrix, i - 1, j, collected, order + [matrix[i][j]], prevDirection
            )
        elif prevDirection == Direction.Right:
            return descend(
                matrix, i, j + 1, collected, order + [matrix[i][j]], prevDirection
            )
        elif prevDirection == Direction.Down:
            return descend(
                matrix, i + 1, j, collected, order + [matrix[i][j]], prevDirection
            )
        else:
            return descend(
                matrix, i, j - 1, collected, order + [matrix[i][j]], prevDirection
            )
    else:
        newDirection = rotate(prevDirection)
        newI, newJ = directionalUpdate(i, j, newDirection)
        collected.add((i, j))
        return descend(
            matrix, newI, newJ, collected, order + [matrix[i][j]], newDirection
        )


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert descend(matrix, 0, 0, set(), [], Direction.Right) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
