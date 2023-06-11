class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    max_count = 0
    count = 0
    founds = {}
    start = 0
    for i in range(len(s)):
      part = s[i]
      
      last_found_index = founds.get(part)
      if last_found_index == None or last_found_index < start:
        count += 1
      else:
        count = i - last_found_index
        start = last_found_index + 1
      
      if count > max_count:
        max_count = count
      
      founds[part] = i

    return max_count
