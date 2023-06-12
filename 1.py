import math

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      dect = {}
      for i in range(len(nums)):
        dect[nums[i]] = i

      for i in range(len(nums)):
        want = target - nums[i]
        want_i = dect.get(want)
        if want_i != None and want_i != i:
          return [i, dect[want]]
