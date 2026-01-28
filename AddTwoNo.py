# leetcode python problem
# Q.2 Add Two Numbers
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution(object):
  def addTwoNumbers(self, l1, l2):
    dummy = ListNode()
    tail = dummy
    
    "setting the carry to zero"
    carry = 0
    "until the list goes on "
    while l1 or l2 or carry:
      val1 = l1.val if l1 else 0
      val2 = l2.val if l2 else 0
      "suppose 4 + 6 = 10"
      total = val1+val2+carry
      "10 // 10 = 1"
      carry = total // 10
      "10 % 10 = 0" 
      digit = total % 10
      
      tail.next = ListNode(digit)
      tail = tail.next
      
      if l1:
        l1 = l1.next
      if l2:
        l2 = l2.next
        
    return dummy.next
