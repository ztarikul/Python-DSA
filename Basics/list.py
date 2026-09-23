
# myList = [1,2,3,4,5]

# # myList.append(6)
# # myList.insert(3,10)  // insert at the index 3 of value 10
# # myList.pop(1) //pop delete the index wise
# # myList.remove() //remove delete the value wise
# # myList.clear()
# # print(myList)

# squares = [x**2 for x in range(1, 10) if x % 2 == 0 ]

# print(sorted(squares))


# Problem 1: Find the Largest and Smallest Number
# Task: Write a function that takes a list of numbers and returns both the smallest and largest numbers without using built-in min() or max() functions.
# Example Input: [12, 45, 2, 67, 34]
# Example Output: (2, 67)

# def find_min_max(numbers):
#     if not numbers:
#         return None

#     smallest = numbers[0]
#     largest = numbers[0]

#     for num in numbers:
#         if num < smallest:
#             smallest = num
#         if num > largest:
#             largest = num
#     return smallest, largest


# nums = [12, 45, 2, 67, 34]
# print(find_min_max(nums))

# Problem 2: Reverse a List In-Place
# Task: Write a function that reverses a list without creating a new list or using the built-in .reverse() method or slicing [::-1].
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [5, 4, 3, 2, 1]

# def reverse_in_place(lst):
#     if not lst:
#         return None

#     left = 0
#     right = len(lst) -1

#     while left < right:
#         # tempLeft = lst[left]
#         # tempRight = lst[right]

#         # lst[left] = tempRight
#         # lst[right] = tempLeft

#         # instead of create any temp variable, 

#         lst[left],lst[right] = lst[right],lst[left]
#         left +=1
#         right -=1

#     return lst

    

# items = [1,2,3,4,5]
# print(reverse_in_place(items))

