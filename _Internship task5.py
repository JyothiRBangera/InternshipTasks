#!/usr/bin/env python
# coding: utf-8

# In[13]:


#to create a function get two integer inputs from user and do arithmetic operation
def num(a,b):
       print("addition of two number:",a+b)
       print("subtraction of two number:",a-b)
       print("multiplication of two number:",a*b)
       print("division of two number:",a//b)
num1=int(input("enter the first number:"))
num2=int(input("enter second number:"))
num(num1,num2)


# In[14]:


#create a function covid()and accept patient name and body temperature
def covid(name,temp=98):
     
    print("patient name:",name)
    print("body temperature:",temp)
    
    
a=input("enter the name of patient:")
b=input("enter the body temperature of patient:")

covid(a,b)


# In[11]:


#create a function covid()and accept patient name and body temperature,by default body temperature should be 98 degree
def covid(name,temp=98):
    
    print("patient name:",name)
    print("body temperature:",temp)
    
    
a=input("enter the name of patient:")


covid(a)


# In[ ]:




