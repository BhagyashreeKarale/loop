#Q-6. Niche diye gye code snippet ki output kya hogi?

x = 0
while(x<7):
    if x == 3 or x==5:
        x = x + 1#increment is necessary even if you continue
        continue
    print(x)
    x = x + 1
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<OUTPUT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
0
1
2
4
6