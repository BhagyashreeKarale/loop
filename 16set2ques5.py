# 1 se 10 tak numbers print karo. Aapka loop ka counter 156 se shuru hona chaiye.
# Aapki output yeh honi chaiye:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# counter=156
# i=counter-155
# while i <=10:
#     print(i)
#     i+=1

#another way without takin another initializer:
counter=156
while counter < 166:#here if we wanted to use <= sign , it should be counter<=165#be careful while using just , and using <=
    num=counter-155
    print(num)
    counter=counter+1
