from queue import LifoQueue

class Solution:
  lefts = {
    '(': 1, 
    '{': 2, 
    '[': 3,
  }
  rights = {
    ')': 1, 
    '}': 2, 
    ']': 3,
  }
  def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0:
      return False
      
    stack = LifoQueue()
    for p in s:
      if stack.qsize() > len(s):
        return False

      left = self.lefts.get(p)
      if left is not None:
        stack.put(left)
        continue

      right = self.rights.get(p)
      if right is None: # unexpected
        return False

      if stack.empty():
        return False

      left = stack.get()
      if left != right:
        return False

    return stack.empty()
