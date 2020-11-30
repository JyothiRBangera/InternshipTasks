#!/usr/bin/env python
# coding: utf-8

# In[26]:


#types of errors 
#SyntaxError:
#indexerror:error caused when trying to access an item at invalid index
#ModuleNotFoundError:caused when module is not defined
#KeyError:caused when key is not found
#ImportError:caused when operation or function is applied to object of appropriate type
#TypeError:caused when operation or function is applied to an object of an appropriate type
#ValeError:caused when a function argument is of appropriate type
#NameError:caused when object is not found
#ZeroDivisionError:caused when second operator in division is zero
#example program for checking all errors 
print"hello"


# In[29]:


#index error
list1=[1,2,3,4]
list1[4]


# In[14]:


import mymodule#modulenotfound error


# In[25]:


dict1={"1":"one","2":"two"}#key error
dict1[3]


# In[16]:


from math import square#import error


# In[18]:


"22"+2#type error


# In[21]:


int("34.0") #value error


# In[22]:


month #name error


# In[23]:


div1=34/0 #zerodivision error


# In[5]:


#design simple calculator by using try and except 
try:
    num1=float(input("enter first number:"))
    num2=float(input("enter second number"))

    c=int(input("enter the users choice:"))
    if c==1:
        print("addition of two numbers is:",num1+num2)
    elif c==2:
        print("subtraction of two numbers is:",num1-num2) 
    elif c==3:
        print("multiplication of two numbers is:",num1*num2)
    elif c==4:
        print("division of two numbers is:",num1/num2)
    elif c==5:
        print("invalid choice")
    else:
        print("enter valid integer")
except NameError:
    print("error occured1")
except TypeError:
    print("error occured2")
except ValueError:
    print("error occured3")
except AttributeError:
    print(" error occured4")
    


# In[35]:


#to print message if try block raises a NameError and another for other error 
try:
    q=input("enter name:")
    print(p)
except NameError:
    print("NameError has occured")
else:
    print("nothing went wrong")


# In[36]:


# try-except is needed to handle exceptions,try lets you to test block of code whereas except block lets you to handle the 
#errors,other than this try-except is not required


# In[39]:


#get an input inside try catch block
try:
    n1=int(input("enter  the first number you choose:"))
    n2= int(input("enter the second number you chhose:"))
    ans=print("by adding two numbers:",n1+n2)
    
except ValueError:
            print("error occured")
    

