#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class coffee_machine:
   water=500
   milk=500
   coffee=650
   total=2.5
   def __init__(self,resource_value ): 
       self.resource_value=resource_value
   def prepare(self,resource_value ,x):
       if(x=="1"):
           self.water=self.water-100
           print(self.water)
           self.milk=self.milk-100
           print(self.milk)
           self.coffee=self.coffee-7
           print(self.coffee)
           self.total=self.total+4.5
           print(self.total)
           print("*****HERE IS YOUR ESPRESSO.ENJOY!******")
       if(x=="2"):
           self.water=self.water-70
           print(self.water)
           self.milk=self.milk-100
           print(self.milk)
           self.coffee=self.coffee-7
           print(self.coffee)
           self.total=self.total+2.5
           print(self.total)
           print("*****HERE IS YOUR  LATTE.ENJOY!******")
            
       elif(x=="3"):
           self.water=self.water-50
           print(self.water)
           self.milk=self.milk-70
           print(self.milk)
           self.coffee=self.coffee-10
           print(self.coffee)
           self.total=self.total+7.99
           print(self.total)
           print("*****HERE IS YOUR CAPPUCINO.ENJOY!******")
           self.report(resource_value,x)
   def report(self,resource_value,x):
           print(f"the status of coffee machine:")
           print(f"{self.water} of water")
           print(f"{self.milk} of milk")
           print(f"{self.coffee} of coffee beans")
           print(f"${self.total} of money")
           self.check(resource_value,x)

   def check(self,resource_value,x ):
       if(resource_value=="espresso"):
           if(self.water<100):
               print("sorry there is not enough of water")
           elif(self.milk<100):
               print("sorry there is not enough of milk")
           elif(self.coffee<70):
               print("sorry there is not enough of coffee")
           else:
               self.coins(resource_value,x)
       elif(resource_value=="latte"):
           if(self.water<70):
               print("sorry there is not enough of water")
           elif(self.milk<100):
               print("sorry there is not enough of milk")
           elif(self.coffee<70):
               print("sorry there is not enough of coffee")
           else:
               self.coins(resource_value,x)
       else:
           if(self.water<50):
               print("sorry there is not enough of water")
           elif(self.milk<70):
               print("sorry there is not enough of milk")
           elif(self.coffee<100):
               print("sorry there is not enough of coffee")
           else:
               self.coins(resource_value,x)
   def coins(self,resource_value,x):
       print("*****TO CALCULATE THE TOTAL AMOUNT PLEASE INSERT YOUR COIN!******:")
       quarter=int(input("enter the money in terms of quarter:"))
       dimes=int(input("enter the money in terms of  dimes:"))
       pennies=int(input("enter the money in terms of  pennies:"))
       nickel=int(input("enter the money in terms of  nickel:"))
       total=(0.25*quarter)+(0.1*dimes)+(0.05*nickel)+(0.01*pennies)
       self.tran(total,x,resource_value)
   
   def tran(self,total,x,resource_value):
       if(x=="1"):
               if(total<4.5):
                   print("sorry,there is not enough of money.money refunded")
               else:
                   print("Here is your change:)",round(total-4.5,2))
                   self.prepare(resource_value,x)
       elif(x=="2"):
           if(total<2.5):
               print("sorry, there is not enough of money.money refunded")
           else:
               print("Here is your change :)",round(total-2.5,2))
               self.prepare(resource_value,x)
       else:
           if(total<7.99):
               print("sorry,there is not enough of money.money refunded")
           else:
               print("Here is your change :)",round(total-7.99,2))
               self.prepare(resource_value,x)
                
x="on" 
s=coffee_machine(x)
while(True):
   y=input("what do you want to buy?1-espresso,2-latte,3-cappuccino,back-to main menu:\n" )
   if(y=="off"):
       break
   if(y=="report"):
       s.prepare(x)
       continue
   s.report(x,y)    

