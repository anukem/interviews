
[Meduim]
[[Interview Question]]

Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown period between two **same tasks** (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.

Return _the least number of units of times that the CPU will take to finish all the given tasks_.

**Example 1:**

**Input:** tasks = ["A","A","A","B","B","B"], n = 2
**Output:** 8
**Explanation:**
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

**Example 2:**

**Input:** tasks = ["A","A","A","B","B","B"], n = 0
**Output:** 6
**Explanation:** On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

**Example 3:**

**Input:** tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
**Output:** 16
**Explanation:**
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

---
I ended up spending the better part of an hour and a half looking at this problem. My original idea was to keep a priority queue of all the tasks with the intent of trying to do the hard task of keeping track of what the time was, and whether or not I could take a specific task at a time t. That turns out to be hard to keep track of long term. So instead the easier thing to do is keep track of what happens in the span of the "cooldown" time. So if n = 3, for every 3 seconds, how many tasks are you able to complete? Obviously if there are enough tasks, you complete 3, but no matter what you will either have completed all your tasks, or only completed as many as you could before having to go idle. So in that way, we can keep chunking out n seconds until all the tasks are completed. If we're interested in the cases where we are idle, its every span of n seconds where we don't have enough tasks to do. I ended up asking ChatGPT to explain, and nothing made sense until I looked at the code I wrote for this back in 2020.


In short, here's an iterative approach to get to the answer
```python
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
```

Will spend at MOST 20 minutes trying to do this functionally, before moving onto something else.

```python
def leastInterval(self, tasks: List[str], n: int) -> int:
      freq = {}
      for task in tasks:
        freq[task] = 1 if task not in freq else freq[task] + 1

      taskCount = [-freq[x] for x in freq]
      heapify(taskCount)
      def task_scheduler(queue, n, count):

        processing = []
        t = n + 1
        while queue and t > 0:
          processing.append(-heappop(queue))
          t -= 1

        for task in reversed(processing):
          task -= 1
          if task != 0:
            heappush(queue, -task)


        if queue:
          return task_scheduler(queue, n, count + n + 1)
        else:
          return count + len(processing)

      return task_scheduler(taskCount, n, 0)
```

At exactly 19 minutes lol
