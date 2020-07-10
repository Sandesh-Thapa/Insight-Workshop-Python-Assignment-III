def linear_search(original, x):
    for i in range(len(original)):
        if original[i] == x:
            return i
    return -1


mainList = [234, 5, 6, 764, 1, 23, 4, 900, 34, 5, 67, 43, 123]
num = int(input("Enter a number to search: "))
result = linear_search(mainList, num)
if result == -1:
    print("Number not found !!!")
else:
    print(f"Number {num} is present at index {result}")
