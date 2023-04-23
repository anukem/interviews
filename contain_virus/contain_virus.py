from pprint import pprint
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
      def isWall(pos, wasGerm):
        x, y = pos
        if x < 0 or x == len(isInfected) or y < 0 or y == len(isInfected[0]):
          return 0
        
        if isInfected[x][y] == 1:
          # is infected and came from germ?
          return 0
        elif isInfected[x][y] == 0 and wasGerm:
          return 1

        return 0
      

      visited = set()
      graph = defaultdict(lambda: [])
      size_graph = defaultdict(lambda: (0, set()))
    
      def explore(pos, isRoot, prevPos, root):
        if pos in visited:
          return

        x, y = pos
        visited.add(pos)
        
        if x < 0 or x == len(isInfected) or y < 0 or y == len(isInfected[0]):
          return
        
        if isInfected[x][y] == 1:
          graph[prevPos].append(pos)
          num_walls = isWall((x, y + 1), True) + isWall((x, y - 1), True)  + isWall((x + 1, y), True)  + isWall((x - 1, y), True) 
          if isWall((x, y + 1), True) == 1:
            size_graph[root][1].add((x, y + 1))
          if isWall((x, y - 1), True) == 1:
            size_graph[root][1].add((x, y - 1))
          if isWall((x + 1, y), True) == 1:
            size_graph[root][1].add((x + 1, y))
          if isWall((x - 1, y), True) == 1:
            size_graph[root][1].add((x - 1, y))
          
          size_graph[root] = (size_graph[root][0] + num_walls, size_graph[root][1])
          explore((x, y + 1), False, pos, root)
          explore((x, y - 1), False, pos, root)
          explore((x + 1, y), False, pos, root)
          explore((x - 1, y), False, pos, root)
      
      

      for x in range(len(isInfected)):
        for y in range(len(isInfected[x])):
          explore((x, y), True, None, (x, y))
      

      max_key, max_seen = None, 0
      for key in size_graph:
        if len(size_graph[key][1]) > max_seen:
          max_seen = len(size_graph[key][1])
          max_key = key
      
      total = 0
      total += size_graph[max_key][0]

      # mark them as seen
      def markContained(root, graph):
        x, y = root
        isInfected[x][y] = -1

        for child in graph[root]:
          markContained(child, graph)
      
      if max_key:
        markContained(max_key, graph)
        graph[None].remove(max_key)

      # move to the next state
      def growVirus(graph, pos):
        x, y = pos
        if isInfected[x][y] == -1:
          return
        if isWall((x, y + 1), True) == 1:
          isInfected[x][ y + 1] = 1
        if isWall((x, y - 1), True) == 1:
          isInfected[x][y - 1] = 1
        if isWall((x + 1, y), True) == 1:
          isInfected[x + 1][y] = 1
        if isWall((x - 1, y), True) == 1:
          isInfected[x- 1][y] = 1


        for child in graph[pos]:
          growVirus(graph, child)

      def advanceToNewDay(graph):
        for root in graph[None]:
          growVirus(graph, root)
      
      def hasNoZeros():
        for x in range(len(isInfected)):
          for y in range(len(isInfected[0])):
            if isInfected[x][y] == 0:
              return False
        return True


      def allVirusContained(graph):
        return len(graph[None]) == 0 or hasNoZeros()

      while not allVirusContained(graph):
        advanceToNewDay(graph)
        size_graph = defaultdict(lambda: (0, set()))
        visited = set()
        roots = graph[None]
        graph = defaultdict(lambda: [])
        for root in roots:
          explore(root, True, None, root)

        max_key, max_seen = None, -1
        for key in size_graph:
          if len(size_graph[key][1]) > max_seen:
            max_seen = len(size_graph[key][1])
            max_key = key
        
        if max_key:
          total += size_graph[max_key][0]
          markContained(max_key, graph)
      
      return total
