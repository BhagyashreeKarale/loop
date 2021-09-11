#from right
i=0
while i <= 4:
    num=1
    while num <= i:
        print(num,end="")#here it is 1 then 12 then 123.but if we want 1 then 22 then 333 we should replace num with i
        num=num+1
    print()
    i=i+1
#from left
i = 1
while i <= 4:
    space=1
    while space <= 4-i:
        print(print="",end="")#here notice the "" make sure it has a space in it.i.e " " like this.end is compulsory as it holds the line.if you want to use only the end make sure it has space in its quotation.
        space=space+1
    num=1
    while num <= i:
        print(i,end="")
        num=num+1
    print()
    i=i+1




