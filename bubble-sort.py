def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


lst = [54, 6, 4, 5, 23, 1, 66, 4, 5]
bubble_sort(lst)
print(lst)
