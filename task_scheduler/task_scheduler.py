def task_scheduler(tasks, n):
    task_map = {}
    for task in tasks:
        task_map[task] = 1 if task not in task_map else task_map[task] + 1

    answer = 0
    queue = [(task_map[task]) for task in task_map]

    while len(queue) != 0:
        queue = sorted(queue, reverse=True)
        completed_tasks = n + 1
        processing = []
        for i in range(n + 1):
            if len(queue) != 0:
                processing.append(queue.pop(0))

        for i in reversed(range(len(processing))):
            if processing[i] - 1 > 0:
                queue.insert(0, processing[i] - 1)

        answer += len(processing) if len(queue) == 0 else completed_tasks

    return answer


assert task_scheduler(["A", "A", "B", "B"], 0) == 4
assert task_scheduler(["A", "B", "B", "B"], 2) == 7
assert task_scheduler(["A", "A", "A", "B", "B", "C"], 2) == 7
