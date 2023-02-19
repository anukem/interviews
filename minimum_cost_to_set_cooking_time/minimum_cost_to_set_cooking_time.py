targetSeconds = 61
startAt = 1
moveCost = 2
pushCost = 1

def get_possible_times(seconds):
    totalMinutes = seconds // 60
    remainingSeconds = seconds % 60
    possibilities = []
    while totalMinutes > 0:
      if totalMinutes <= 99 and remainingSeconds <= 99:
        possibilities.append((totalMinutes, remainingSeconds))

      totalMinutes -= 1
      remainingSeconds += 60

    if remainingSeconds <= 99:
      possibilities.append((0, remainingSeconds))

    return possibilities


def convert_possible_times_to_path(time):
    minute, seconds = time

    seconds_with_zeroes = "0" + str(seconds) if seconds < 10 else str(seconds)
    paths = []
    if minute == 0:
      if seconds < 10:
        paths.append(str(seconds))

      paths.append(seconds_with_zeroes)
      paths.append("0" + str(minute) + seconds_with_zeroes)
      paths.append(str(minute) + seconds_with_zeroes)
    elif minute < 10:
      paths.append("0" + str(minute) + seconds_with_zeroes)
      paths.append(str(minute) + seconds_with_zeroes)
    else:
      paths.append(str(minute) + seconds_with_zeroes)


    return paths

def reduce_cost(path, collectedCost, prevValue):
    if not path:
      return collectedCost

    if str(prevValue) == path[0]:
      collectedCost += pushCost
    else:
      collectedCost += moveCost
      collectedCost += pushCost

    return reduce_cost(path[1:],  collectedCost, path[0])

def calculate_cost(paths):
    costs = []
    for path in paths:
      costs.append(reduce_cost([num for num in path], 0, startAt))

    return min(costs)



paths = [convert_possible_times_to_path(time) for time in get_possible_times(targetSeconds)]

costs = [calculate_cost(path) for path in paths]

assert min(costs) == 6

