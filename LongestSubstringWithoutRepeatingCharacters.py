# leetcode python problem
# Q.3 Longest Substring Without Repeating Character
class Solution(object):
  def lengthOfLongestSubstring(self, s):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
      
      "if value in s is present in the seen"
      while s[right] in seen:
        seen.remove(s[left])
        left=+1
        
      "else add the value in the seen"  
      seen.add(s[right])
      
      max_len = max(max_len, right - left +1)
    return max_len
