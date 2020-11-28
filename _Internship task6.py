#!/usr/bin/env python
# coding: utf-8

# In[10]:


#program to loop through a list of number and add +2 t0 every value element in the list
num=[100,56,90]
print(num)
res=[]
for i in range(0,len(num)):
    res.append(num[i]+2)
print(res)


# In[1]:


#to get below pattern
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()


# In[16]:


#to print fibonacci sequence
x=int(input("enter the number:"))
temp=0
a=0
b=1
if(x<=0):
    print("enter the positive number:")
elif x==1:
     print(b)
else:
    print("fibonacci sequence:")
    while temp<x:
        print(a)
        
        c=a+b
        a= b
        b=c
        temp=temp+1
    
   
        

   


# In[1]:


#Armstrong number is sum of cubes of its digits is the number itself.Here consider an example of 150=1^3+5^3+0^3=126
#hence "150" is not an Armstrong number.in first iteration d=0 and s=0+0^3=0 and temp=150/10=15.by checking if condition 150!=0.
#second iteration checking the while loop condition 15>0 true,d=5,s=0+5^3=125  ,temp=1 checking if condition 1!=125
#in third iteration 1>0,d=1,s=126,temp=0,checking if condition 0!=126 hence checking while condition 0>0 come out of the loop 
#and print else statement 150 is not an Armstrong number
num2=int(input("enter number:"))
s=0
temp=num2
while temp>0:
    d=temp%10
    s+=d**3
    temp//=10

if num2==s:
    print(num2,"is an Armstrong number")
else:
    print(num2,"is  not an Armstrong number")
    


# In[2]:


#to print multiplication table of 9
n=9
for i in range(1,11):
    print(n,'*',i,'=',n*i)
    


# In[3]:


#to check the number is negative or positive
num=int(input("enter the number"))
if(num>0):
    print("positive number")
else:
    print("negative number")


# In[13]:


#to convert days to ages
x=int(input("input for days="))
print("number of years=",x/365)


# In[32]:


#trigonometry problem using math function
import math
x=9
print("sine of pi/6 is:",math.sin(math.pi/6))
print("radians of x is:",math.radians(x))


# In[50]:


#calculator code using if condition(basic arithmetic calculation)
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

