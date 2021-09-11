#pattern print
# num = int(input("Enter number of rows"))
# row = 0
# while row < num:
#     space = num - row - 1
#     while space > 0:
#         print(end=" ")
#         space = space - 1
#     star = row + 1
#     while star > 0:
#         print("*",end=" ")
#         star = star - 1
#     print()
#     row = row + 1
# row=num
# while row>0:
#     space = num-row+1
#     while space>0:
#         print(" ",end="")
#         space = space - 1
#     star=row-1
#     while star>0:
#         print("*",end=" ")
#         star = star - 1
#     print()
#     row=row-1
#note:
# space,star,row,and num updation and values
# print()
# space in end=""
##############################################################################################################
#number print
# num=int(input("Enter number of rows"))
# row=0
# while row<num:
#     space=num-row-1
#     while space>0:
#         print(" ",end="")
#         space=space-1
#     star=row+1
#     while star>0:
#         print(row+1,end=" ")
#         star=star-1
#     print()
#     row=row+1




row=4
num=0
while num<row:
    space=row-num-1
    while space>0:
        print(end=" ")
        space=space-1
    star=row-space
    while star>0:
        print("*",end=" ")
    star=star-1
    print()
    num=num+1