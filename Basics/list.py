
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



# Problem 3: Remove Duplicates While Preserving Order
# Task: Write a function that removes duplicate values from a list while keeping the original order of elements intact.
# Example Input: [1, 2, 2, 3, 4, 3, 5]
# Example Output: [1, 2, 3, 4, 5]


# def remove_duplicate(lst):

#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)

#     return result
    

#     # return list(set(lst))


# lst = [1,2,2,3,4,3,5]
# print(remove_duplicate(lst))


# Problem 4: Filter Even Numbers (List Comprehension)
# Task: Given a list of integers, return a new list containing only the even numbers, using a list comprehension.
# Example Input: [1, 2, 3, 4, 5, 6, 7, 8]
# Example Output: [2, 4, 6, 8]

# def get_integer(lst):

#     # result = []

#     # for item in lst:

#     #     if item % 2 == 0:
#     #         result.append(item)

#     # return result

#     # alternate
#     return [x for x in lst if x % 2 == 0]

# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# print(get_integer(lst))


# Problem 5: Flatten a 2D Matrix
# Task: Write a function that takes a nested list (a matrix of rows and columns) and flattens it into a single 1D list.
# Example Input: [[1, 2], [3, 4], [5, 6]]
# Example Output: [1, 2, 3, 4, 5, 6]

# def flatten_matrix(grid):

#     flatten = []

#     for row in grid:
#         for item in row:
#             flatten.append(item)

#     return flatten


# grid = [[1, 2], [3, 4], [5, 6]]
# print(flatten_matrix(grid))