#!/usr/bin/env python
# coding: utf-8

# In[1]:


#using zip()function and list() create merged list of tuples from two lists given
a=[10,12,23]
b=[1,63,5]
print(list(zip(a,b)))
 


# In[7]:


#create a range from 1 to 8 then using zip function, merge the given list and range together to create a new list of tuples
x=range(1,8) 
list1=[7, 9, 23, 4, 59, 96, 100]
print(list(zip( x,list1)))


# In[3]:


#using sorted() function sort list in ascending order
a=[15,56,7,75,100,25,69]
print(sorted(a))


# In[4]:


#using filter function,filter the even number so that only odd numbers are passed to new list
list1=[14,5,23,3,9,65,4,18]
new_list=list(filter(lambda x:x%2!=0,list1))
print(new_list)

