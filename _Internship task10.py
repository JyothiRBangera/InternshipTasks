#!/usr/bin/env python
# coding: utf-8

# In[11]:


#to check a string contains only a certain set of characters(in this case a-z,A-Z and 0-9)
import re
print(bool(re.match('^[A-Za-z0-9]*$',"123aAbc097")))
print(bool(re.match('^[A-Za-z0-9]*$',"AP^!#PL23E")))


# In[12]:


#program that matches a word containing'ab'
import re
def abmatch(text):
    pattern="ab"
    if re.search(pattern,text):
        return('found a match!') 
    else:
        return('not matched!')
print(abmatch("abcab"))  
print(abmatch("urt"))
print(abmatch("ertuab"))
 


# In[2]:


#to check for a number at end of word/sentence
import re
def num(wrd):
    z=re.compile(r".*[0-9]$")
    if z.match(wrd):
        return True
    else:
        return False
print(num("55abcab"))  
print(num("ur2666t100"))
print(num("ertuab45"))
 


# In[7]:


#to search the number(0-9)of length between 1 to 3 in a given string
import re
txt="lointou179k125 45569"
search=re.findall(r'[0-9]{1,3}',txt)
print(search)


# In[10]:


#to match a string that contains only uppercase letters
import re
str1=input("enter the string of your choice:")
srch=re.findall("[A-Z]",str1)
print(srch)
 

