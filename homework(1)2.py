from random import randint as kd

a = kd(0,11)
b = kd(0,11)
c = kd(0,11)

if a > b:
    print("everything will be fine")
elif a < b:
    print("this is terrible")
elif a == b:
    print(c,"teper eta")
    if (a + b) < c:
        print("I am cool")
    elif (a + b) > c:
        print("I am ugl")
    elif (a + b) == c:
        print("stradaniye")