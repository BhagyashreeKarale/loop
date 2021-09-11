# Ek program banao jo 1 se 100 tak ke beech mein woh numbers print kare jo 7 se divide ho jaate hain.
# Note: Aap jo loop likhoge uska counter 556 se start hona chaiye.
# Aapki output mein yeh aana chaiye.
# 7
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63
# 70
# 77
# 84
# 91
# 98
counter=556
i=counter-556#here we took another variable which initializes 0 as starter as that is more conveninent
while i<=100:
    if i%7==0:
        print(i)
    i+=1
#another method:without changing initializer
counter=556
while counter<=656:
    i=counter-555
    if i % 7 == 0:
        print(i)
    counter=counter+1