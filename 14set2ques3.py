# Ek program banao jo 1 se 100 tak ke numbers ke saath yeh kare:
# Jo 3 se divisible hain unki jagah "Nav" print kare
# Jo 7 se divisible hain unki jagah "Gurukul" print kare
# Jo 3 aur 7 dono se divisible hain, unki jagah "NavGurukul" print karein# Jo upar wale teen cases mein nahi aate, unki jagah sirf number print karvao.
# Aapki output mein kuch aisa aana chaiye.
# 1
# 2
# Nav
# 4
# 5
# Nav
# Gurukul
# 8
# Nav
# 10
# 11
# Nav
# 13
# Gurukul
# Nav
# 16
# 17
# Nav
# 19
# 20
# NavGurukul
# 22
# 23
# Nav
# 25
# 26
# Nav
# Gurukul
# 29
# Nav
# 31
# 32
# Nav
# 34
# Gurukul
# Nav
# 37
# 38
# Nav
# 40
# 41
# NavGurukul
# 43
# 44
# Nav
# 46
# 47
# Nav
# Gurukul
# 50
# Nav
# 52
# 53
# Nav
# 55
# Gurukul
# Nav
# 58
# 59
# Nav
# 61
# 62
# NavGurukul
# 64
# 65
# Nav
# 67
# 68
# Nav
# Gurukul
# 71
# Nav
# 73
# 74
# Nav
# 76
# Gurukul
# Nav
# 79
# 80
# Nav
# 82
# 83
# NavGurukul
# 85
# 86
# Nav
# 88
# 89
# Nav
# Gurukul
# 92
# Nav
# 94
# 95
# Nav
# 97
# Gurukul
# Nav
# 100
counter = 1
while counter <= 100:
    if counter %3 == 0 and counter % 7 == 0:#dont forget ==0
        print("NavGurukul")
    elif counter % 7 == 0 and counter % 3 != 0:
        print("Gurukul")
    elif counter % 3 == 0 and counter % 7 != 0:
        print("Nav")
    else:
        print(counter)
    counter+=1