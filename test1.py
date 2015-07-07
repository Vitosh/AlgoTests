myInput = input()
numbers = myInput.split()
numbers = [int(i) for i in numbers]
print(sum(numbers))