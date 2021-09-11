# Iss question ke saath solution di hui hai. 
# Yeh aapko samjhane ke liye hai ki hum iss type ke questions kaise solve kar sakte ho. 
# Better yeh hoga ki aap solution na dekho aur pehle khud solve karne ki try karo.

# Solution se pehle ek chota sa concept samajhte hain. 
# Jaise agar hum 4*3 karte hain toh hum 2 integers ko multiply kar rahe hain aur humara result 12 aayega. 
# Aise hi agar hum ek string aur integer ko different behaviour hoga. 
# Jaise
# >>> 'navgurukul' * 3
# 'navgurukulnavgurukulnavgurukul'
# Dekho kaise "navgurukul"*3 karke navgurukul 3 baar aa gaya. 
# Aise hi 'hello'*5 hello 5 baar ayega. 
# Jaise:
# >>> 'hello' * 5
# 'hellohellohellohellohello'
# Yeh program likhne se pehle upar wale pattern mein kuch cheezein dekhte hain.

# Pehli, iss pattern mein total 7 lines hain.

# Pehli line mein ek # hai, dusri line mein 2 # hain, teesri line mein 3 # hain.

# Matlab number of # bhi line number ke saath badte jaa rahe hain.

# Iska solution kuch aisa hoga.


# i = 1 # counter 1 se shuru karo
# while i <= 7: # kyunki humare program mein 7 lines hain isliye loop tab hi band karna hai jab woh 7 baar chal jaye. Har baar line print karne pe loop chalega.
#   print('#'*i)#utne time print hoga jitna uska sequence mai number hai(i ki value).i.e.# will be printed 1 times if the counter is 1,
#   i = i + 1   #2 times if the counter is 2 
  
# user_input=int(input("enter number"))
# i=1
# while i<=user_input:
#   b=int(user_input)
#   c=str(b)
#   print(c*i)
#   i+=1
#   b-=1

# user_input=int(input("number"))
# i=1
# while i<=user_input:
#   print(str(i)*i)
  # i+=1
#another way:
user_input=int(input("Enter number of rows"))
i=1
while i <= user_input:
  j=1
  while j <= i:
    print(j,end="")#dont forget the end="" as it hold on the line
    j=j+1
  print()#dont forget blank print as it indicates for new line
  i=i+1
#here you can print the following patterns:
# for i:
# 1
# 22
# 333
# 4444
# for j:
# 1
# 12
# 123
# 1234
# for same number:
# 1
# 11
# 111
# 1111