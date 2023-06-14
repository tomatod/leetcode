import itertools

class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    patterns = ['']
    open_num = [0]
    left_use = [0]
    right_use = [0]
    for i in range(n*2):
      new_patterns = []
      new_left_use = []
      new_right_use = []
      for j in range(len(patterns)):
        if left_use[j] < n:
          new_patterns.append(patterns[j] + '(')
          new_left_use.append(left_use[j] + 1)
          new_right_use.append(right_use[j])
        if right_use[j] < left_use[j]: 
          new_patterns.append(patterns[j] + ')')
          new_left_use.append(left_use[j])
          new_right_use.append(right_use[j] + 1)

      patterns = new_patterns
      left_use = new_left_use
      right_use = new_right_use

    return patterns
