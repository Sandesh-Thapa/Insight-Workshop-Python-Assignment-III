def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1


mainList = [2, 3, 4, 10, 40]
num = int(input("Enter a number to search: "))
result = binarySearch(mainList, 0, len(mainList) - 1, num)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
