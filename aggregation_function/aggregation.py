unused_ints = {}

def traverse(arr, blocks, i, j):

  if i == len(arr):
    return blocks

  curr = arr[i]
  current_block = blocks[j]

  if not current_block:
    current_block.append(curr)
    return traverse(arr, blocks, i + 1, j)

  if current_block[-1] + 1 == curr:
    current_block.append(curr)
    return traverse(arr, blocks, i + 1, j)

  blocks.append([])
  return traverse(arr, blocks, i, j + 1)

def process(arr):
  arr.sort()
  blocks = traverse(arr, [[]], 0, 0)

  gaps = []
  for i, block in enumerate(blocks):
    gaps.append((block[0] - 1, i, -1))
    gaps.append((block[-1] + 1, i , 1))
    if len(block) < 2:
      val = block[0]
      if val not in unused_ints:
        unused_ints[val] = 1
      else:
        unused_ints[val] += 1
        

  for (gap, i, direction) in gaps:
    if gap in unused_ints:
      if direction == 1:
        blocks[i].append(gap)
      else:
        blocks[i].insert(0, gap)




  def merge(left, right):
    if left[-1] == right[0]:
      return left + right[1:], left[-1]

    return None, None

  start = 0
  end = start + 1


  while end < len(blocks):

    merged, val = merge(blocks[start], blocks[end])
    
    if merged:
      del blocks[start]
      del blocks[end - 1]
      blocks.insert(start, merged)
      unused_ints[val] -= 1
      
      end += 1
    else:
      start += 1
      end += 1

  return list(filter(lambda x: len(x) >= 2, blocks))



print(process([9, 6,7]))
print(process([7,8, 10, 11]))
print(process([2]))
print(unused_ints)
  
