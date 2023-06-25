#!/usr/bin/env python
# coding: utf-8

# In[ ]:


QUESTION:-
    
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
    
Example 2:

Input: s = "loveleetcode"
Output: 2
    
Example 3:

Input: s = "aabb"
Output: -1


# In[ ]:


ANSWER:-


# In[4]:


import collections
class Solution(object):
    def firstUniqChar(self, s):
        set = collections.Counter(s);
        # Traverse the string from the beginning...
        for i in range(len(s)):
            # If the count is equal to 1, it is the first distinct character in the list.
            if set[s[i]] == 1:
                return i
        return -1       # If no character appeared exactly once...


# In[5]:


obj = Solution()


# In[6]:


obj.firstUniqChar("leetcode")


# In[8]:


obj.firstUniqChar("HeHii")


# In[ ]:




