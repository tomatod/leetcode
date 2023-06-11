class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
      first = None
      priv  = None
      is_up = False
      while True:
        if l1 is None and l2 is None and not is_up:
          break

        val = 0
        if l1 is not None:
          val += l1.val
        if l2 is not None:
          val += l2.val
        if is_up:
          val += 1
        
        is_up = val >= 10
        val = val % 10

        n = ListNode(val, None)
        if priv is None:
          first = n
        else:
          priv.next = n
        priv = n

        if l1 is not None:
          l1 = l1.next
        if l2 is not None:
          l2 = l2.next
      return first
