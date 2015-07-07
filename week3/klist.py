def compare(a, b, c):
    print("--------")
    print(a)
    print(b)
    print(c)
    Lowest = "Nope"

    if a != "Nope":
        Lowest = a
    if b != "Nope":
        if Lowest == "Nope":
            Lowest = b
        elif b < Lowest:
            Lowest = b
    if c != "Nope":
        if Lowest == "Nope":
            Lowest = c
        elif c < Lowest:
            Lowest = c
    return Lowest

list1 = [8123, 1, 0]
list2 = [3, 5, 2, 213123, 123]
list3 = [2, 56, 3, 1, 12302, 2, 5, 2, 5, 500, 5, 5, 4]

list1.sort()
list2.sort()
list3.sort()

initialLen = len(list1) + len(list2) + len(list3)
sortedList = []

for i in range(0, initialLen):
    if not list1:
        list1.append("Nope")
    if not list2:
        list2.append("Nope")
    if not list3:
        list3.append("Nope")

    popMe = compare(list1[0], list2[0], list3[0])

    if popMe == list1[0]:
        sortedList.append(list1.pop(0))

    elif popMe == list2[0]:
        sortedList.append(list2.pop(0))

    elif popMe == list3[0]:
        sortedList.append(list3.pop(0))

print(sortedList)
