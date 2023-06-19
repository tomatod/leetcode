# first answer
import math

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    max_index = len(nums) - 1
    min_index = 0
    if target >  nums[max_index]: return max_index + 1
    if target == nums[max_index]: return max_index
    if target <= nums[min_index]: return 0
    while max_index - min_index > 1:
      marker_index = math.ceil((max_index + min_index) / 2)
      marker = nums[marker_index]
      if target == marker: return marker_index
      if target > marker:
        min_index = marker_index
        continue
      max_index = marker_index
    return max_index

# refactored
class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    max_index = len(nums) - 1
    min_index = 0
    while max_index >= min_index:
      marker_index = (max_index + min_index) // 2
      marker = nums[marker_index]
      if target == marker: return marker_index
      if target >  marker: min_index = marker_index + 1
      else:                max_index = marker_index - 1
    return min_index

# half-open ver
class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    ng = len(nums)
    ok = 0
    while ng - ok > 1:
      mid = (ng + ok) // 2
      if target < nums[mid]: ng = mid
      else:                  ok = mid
    if target > nums[ok]: return ok + 1
    else:                 return ok
