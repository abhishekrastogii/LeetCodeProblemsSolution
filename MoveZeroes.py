#!/usr/bin/env python
# coding: utf-8

# In[ ]:


QUESTION:- 

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


# In[ ]:


ANSWER:-


# In[1]:


class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        for i in range(0,n):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
        return nums


# In[2]:


obj = Solution()


# In[4]:


obj.moveZeroes([1,2,0,98,0,5,6])

