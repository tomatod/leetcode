import math 

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    bigger_than_last = target >= nums[len(nums)-1]
    min_index = 0
    max_index = len(nums)-1
    last = nums[max_index]
    if target == last: return max_index
    while max_index - min_index > 1:
      marker_index = math.ceil((min_index+max_index)/2)
      marker = nums[marker_index]
      if marker == target: return marker_index
      if bigger_than_last:
        if marker <= last:
          max_index = marker_index
        else:
          if target <= marker:
            max_index = marker_index
          else:
            min_index = marker_index
        continue
      else:
        if marker <= last:
          if target <= marker:
            max_index = marker_index
          else:
            min_index = marker_index
        else:
          min_index = marker_index
    if nums[max_index] == target: return max_index 
    if nums[min_index] == target: return min_index 
    return -1
