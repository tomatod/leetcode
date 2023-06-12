class Solution:
  def convert(self, s: str, numRows: int) -> str:
    result = ''
    mx = wd = 2*(numRows-1)
    init = 0
    if mx == 0:
      mx = 1

    l = len(s)
    for i in range(numRows):
      j = i
      wd = init
      while j < l:
        result += s[j]
        if wd != mx:
          wd = mx - wd
        j += wd
      init += 2 % mx

    return(result)
