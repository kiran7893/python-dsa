from util import time_it

@time_it
def linear_search(number_list, key):
    for i in range(len(number_list)):
        if number_list[i] == key:
            return i
    return -1

@time_it
def binary_search(numbers_list, key):
    left = 0
    right = len(numbers_list) - 1
    while left <= right:
        mid = (left + right) // 2
        
        if numbers_list[mid] < key:
            left = mid + 1
        elif numbers_list[mid] > key:
            right = mid - 1
        else:
            return mid
    return -1

@time_it
def binary_search_recursive(numbers_list, key, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if numbers_list[mid] == key:
        return mid
    elif numbers_list[mid] < key:
        return binary_search_recursive(numbers_list, key, mid + 1, right)
    else:
        return binary_search_recursive(numbers_list, key, left, mid - 1)

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,28,39,40,50,60,70,80,89,91,92,93,94]
val = 93

index = linear_search(list1, val)
print(index)

index2 = binary_search(list1, val)
print(index2)

index3 = binary_search_recursive(list1, val, 0, len(list1)-1)
print(index3)
