class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    length = len(nums)
    max_index = length-1
    marker = max_index-1
    while marker >= 0:
      index = marker+1
      while index < length:
        temp = nums[index]
        if temp > nums[marker]:
          nums[index] = nums[marker]
          nums[marker] = temp
          return
        index += 1
      
      reseted = nums[marker:max_index+1]
      reseted.sort()
      nums[marker:max_index+1] = reseted
      marker -= 1 
