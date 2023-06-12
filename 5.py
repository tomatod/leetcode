class Solution:
  max = 2**31 - 1
  min = -2**31
  ascii_codes = {i+48:i for i in range(10)}
  pluse = 43
  minus = 45
  space = 32
  
  def myAtoi(self, s: str) -> int:
    sign = 1
    result = 0
    found_digits = False
    ss = s.encode('ascii')
    for p in ss:
      digit = self.ascii_codes.get(p)
      if digit != None:
        result = result * 10 + digit
        found_digits = True
        continue
      if found_digits:
        break
      if p == self.space:
        continue
      if p == self.minus and not found_digits:
        sign = -1
        found_digits = True
        continue
      if p == self.pluse and not found_digits:
        found_digits = True
        continue
      break
    result = sign * result
    if result > self.max:
      return self.max
    if result < self.min:
      return self.min
    return result
