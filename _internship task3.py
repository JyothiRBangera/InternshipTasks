#!/usr/bin/env python
# coding: utf-8

# In[22]:


#to merge two python dictionaries
c={"colour1":"red","colour2":"black","colour3":"blue"}
f={"fruit1":"apple","fruit2":"mango","fruit3":"pineapple"}
c.update(f)
print(c)


# In[24]:


#to remove a key from dictionary
num1={"one":1,"two":2,"three":3}
print(num1)
num1.pop('two')
print(num1)


# In[34]:


#to map two lists into dictionary
keys=["jerry","tom","bheem"]
values=[20,40,80]
z=dict(zip(keys,values))
print(z)


# In[42]:


#to find length of the set
s=input("enter a string:")
print("length of string:",len(s))


# In[49]:


#to remove intersection of 2nd set from the 1st set
s1={ 40,70,60}
print(s1)
s2={50,40,70,10}
print(s2)
s1.difference_update(s2)
print(s1)


# In[ ]:




