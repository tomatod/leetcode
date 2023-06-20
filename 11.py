from typing import *
import copy

class Solution:

  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    if target == 1: return []
    combinations_by_value = [[] for _ in range(target)]
    for value in candidates:
      if value > target: continue
      index = value - 1
      combinations_by_value[index].append([value])
      diff_max_value = target - value
      for diff_index in range(diff_max_value):
        combinations = combinations_by_value[diff_index] 
        for combination in combinations:
          cp_combination = copy.deepcopy(combination)
          cp_combination.append(value)
          combinations_by_value[index+diff_index+1].append(cp_combination)

    return combinations_by_value[target-1]
