weather = (1, 0, 1, 1, 0, 1, 0,)
sunny = 0
rainy = 0
for x in weather:
    if x == 0:
        rainy += 1
    else:
        sunny += 1

if sunny > rainy:
    print("Weather is good.")
else:
    print("Weather is rainy.")