#Ek program likho jo loop ka use kar ke 1 se leke 100 tak saare numbers ka sum print kare.
# Aapke program ko pehle 1 se 100 ke beech mein saare numbers ka sum calculate karna hai. 
# 1+2+3+4 +5+6+7....+95+96+97+98+99+100 Fir uss sum ko print karana hai.
a = 1
sum = 0 
while a <= 100: 
    if a==100:#important
        print(sum)
    sum = sum + a 
    a = a + 1
   