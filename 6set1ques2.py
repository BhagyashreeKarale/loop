# Ek program banao jo 1 se 100 tak ke beech mein woh numbers print kare jo 7 se divide ho jaate hain.
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
counter = 1#if we start form 0,it is also printed,we want numbers from 1
while counter<= 100:
    if counter % 7 == 0 :
        print(counter)
    counter+=1#dont forget increment
print("These are numbers from 1-100 which are divisible by 7")