intNight1 = int(input())
intNight2 = int(input())

if intNight1 == 0 or intNight1%2 == 0:
    print("yes")
elif intNight2%2 == 1:
    print("yes")
else:
    print("no")