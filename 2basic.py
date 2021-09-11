counter = 0
while counter < 5:
    print ("navgurukul")
    counter = counter + 1
# Iss code mein: 
# 1.counter naam ka ek variable define ho raha hai jiski value 0 hai. Flowchart mein bhi same cheez ho rahi hai.
# 2.Fir ek while loop likha hai jiske aage ek condition hai counter < 5. 
# While ka matlab ho jab tak (जब तक).
# Toh ek tareeke se while loop python ko bolta hai ki jab tak aage di hui condition True hai tab tak loop chalao. 


#####################################################################################################################


# 3.Jaise hi loop khatam hoga toh while ke bahar wala code chalega. Yeh samajhne ke liye neeche diye hua code chalao:
counter = 0 
while counter < 5:
    print ("NavGurukul")
    counter = counter + 1
print ("one time print")
# Yeh code chala ke dekhoge toh "NavGurukul" 5 baar print hoga aur last waali line sirf ek baar.


######################################################################################################################


# Ek aur example
# Maan lo humne code likhna hai jisme humne 1 se 100 tak saare number print karne hai jo 2 se divide hote hain. 
# Toh hum while loops ka use kar ke aise likhenge:
counter = 1
while counter < 100:
    if counter % 2 == 0:
        print (counter)
    counter = counter + 1
# Note: Yahan humne counter 1 se isliye shuru kiya hai kyunki humne 1 se 100 tak print karne hai aur na ki 0 se 99 tak.


######################################################################################################################


# Take an example of getting laptops from a car to the house. If there are 50 laptops in the car.
# Explain this from the concept of Jab tak:
# Jab tak (ghar mein laptops 0 nahi ho jaate){tab tak laptops lao aur gaadi mein rakho.}

# Kaam baar baar karna hai.
# But kitni baar karna hai? Woh jab tak se decide hota hai.
# Jab tak mein jo condition daalte hain tab tak kaam hota hai.
# Yahan jab tak mein hum laptops laptops >= 10 likhenge.
# Matlab jab laptops 10 ya 10 se zyada hain tab jab tak ke andar wala kaam karna band kar do.
# Jab tak ke andar wala kya kaam hai. Andar wala kaam hai laptop lana ghar se aur laptop ko gaadi mein rakh dena.
# Jaisa hi aisa hota ek laptop kam ho jayega.
# Hum isi ki python mein likhna seekhenge.

# Take the example of teaching this in python:
# Let's say total laptops are 10. Laptops = 0. Yeh maintain karega abhi gaadi mein kitne laptops hain.
# Jab tak laptops 10 nahi ho jaate. Tab tak laptops laao aur gaadi mein rakho.
# Matalb while laptops >= 10. This will make sure this work happens for for 10 times.
# Kya kaam karna hai? Laptops gaadi mein rakhna. Print karo "Ek laptop gaadi mein rakh diya"
# Fir kaise track rakhenge ki laptop rakh dia. Aur ek baar kaam kar lia hai.
# Uske liye hum laptop wale variable mein +1 kar denge. Matlab utne laptops humne gaadi mein rakh die hain.
# Let's do the dry run of the same program to see if this works fine.
#i    while   counter   print             counter(increment)
#0                     0 done        0+1=1
#1    >=10      1      1 done        1+1=2
#2    >=10      2      2 done        2+1=3
#3    >=10      3      3 done        3+1=4
#4    >=10      4      4 done        4+1=5
#5    >=10      5      5 done        5+1=6
#6    >=10      6      6 done        6+1=7
#7    >=10      7      7 done        7+1=8
#8    >=10      8      8 done        8+1=9
#9    >=10      9      9 done        9+1=10
#10   >=10      10    10 done        10+1=11 FALSE
# Second we will write the same program in the python visualiser to see if it works the same way as we thought it would. 
# And now explain how the visualiser would run this code.
i=0
while i<=10:#signs are important
    print(i,"done")
    i=i+1
print("finished")
#will start from 0
i=1
while i<=10:#signs are important
    print(i,"done")
    i=i+1
print("finished")
#will start from 1


#########################################################################################################################


#Similarly take another example of printing numbers from 1 to 20:
counter=1
while counter<=20:
    print(counter)
    counter+=1
print("done")



#########################################################################################################################



#Take another example on how printing the even numbers from 20 to 40:
counter=20
while counter<=40:
    if counter%2==0:
        print(counter)
    counter+=2
print("these are even numbers b/w 20 and 40")
