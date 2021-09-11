# Counter Examples
# Iss section mein kuch kuch examples die hue hain. 
# Inn examples ko aapko ache se samajhna chaiye yeh figure out karne ke liye ki yeh kaise kaam karte hain. 
# Aapko har example ka dry run karke dekhna chaiye ki dry run kaise ho raha hai.
# Saath saath comments mein aap kuch aur examples bhi likh sakte hain 
# jisse aapke concepts aur aapke peers ke concepts better clear ho sakte hain.
#####################################################################################################################
# Example 1
# 1 se 40 ke beech ke saare 3 ke multiples print karne hain. 
# Code likhte waqt yeh dhyan rakhein ki aapka counter 891 se shuru hona chaiye.

#Solution to Example 1:
i = 891
while i < 931:#931 is 891+40 (as we want multiples of 3 in b/w numbers 1 to 40)
  z = i - 890
  if z % 3 == 0:
    print(z)
  i = i + 1
######################################################################################################################
#Example 2
#1 se 50 ke beech ke saare 5 ke multiples print karo. 
# Lekin aapko % (modulous operator) ka use nahi karna hai. Uske bina karo.

#Solution to Example 2
i = 0
while i <= 50:
  if i != 0:
    print(i)
  i = i + 5
#####################################################################################################################
#Example 3
#50 se 100 ke beech ke saare odd numbers ka sum print karo.

#Solution 1 to Example 3
#increment=+2
i = 49
while i <= 98:
  i = i + 2
  print(i)
#####################################################################################################################
#Solution 2 to Example 3
#increment=+1
i = 50
while i <= 100:
  if i % 2 != 0:
    print(i)
  i = i + 1
#####################################################################################################################
#Solution 3 to Example 3
#increment=-1
i = 400
while i >= 350:
  z = i - 300
  if z % 2 != 0:
      print(z)
  i = i - 1
######################################################################################################################
#Example 4
#1 se 10 tak number print karne hai .increment ka use nahi karna hai .

#Solution 1 to Example 4
#different ways to implement increment +1
a = -1
while a >= (-10):
    print (-a)#till here the number will be negative.i.e.for eg:-1#but we are printing -(a) .i.e.-(-1)=+1
    a = a -1
#Solution 2 to Example 4
a = 1 
while a <= 10:
    print (a)
    a = a-(-1)#=a+1
#Solution 3 to Example 4
a = 1
while a !=11:
    print (a)
    a-=-1#a=a-(-1)=a+1