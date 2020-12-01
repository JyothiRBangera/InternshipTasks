#!/usr/bin/env python
# coding: utf-8

# In[1]:


#to create lambda function that multiplies argument x with y
num=lambda x,y:x*y
print(num(2,6))


# In[2]:


#to create Fibonacci series to n using Lambda
from functools import reduce
fibnum=lambda m:reduce(lambda x,_:x+[x[-1]+x[-2]],range(m-2),[0,1])
print(fibnum(9))


# In[3]:


#to multiply each number of given list with a given number
num=[1,4,6,53]   
mul=list(map(lambda x:x*3,num))
print("Now the multiplied numbers are:",mul)


# In[4]:


#to find number divisible by 9 from list of number
num=[1,2,3,4,5,6,9,7,59,10,11,27,13,63,15]
div=list(filter(lambda x:x%9==0,num))
print("the number divisible by 9:",div)
     


# In[5]:


#to count even number in given list of integers
num=[1,2,3,4,5,6,9,7,59,10,11,27,13,63,15]
even=list(filter(lambda x:x%2==0,num))
print("the even numbers in a given list:",even)


# In[ ]:




