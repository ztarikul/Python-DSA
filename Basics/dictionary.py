# user = {
#     "name": "Alice",
#     "age": 25,
#     "skills": ["Python", "SQL"]
# }

# print(user['name'])
# print(user.get('age'))
# print(user.get('role', 'N/A'))

# Problem 1: Beginner Level
# Task: Write a function count_frequencies(words) that takes a list of strings and returns a dictionary where keys are the words and values are the number of times each word appears in the list.
# Example Input: ["apple", "banana", "apple", "cherry", "banana", "apple"]
# Expected Output: {"apple": 3, "banana": 2, "cherry": 1}

# def count_frequencies(words: list) -> dict[str, int]:
#     freq = {}

#     for word in words:
#         freq[word] = freq.get(word, 0) + 1

#     return freq
    


# input_words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# print(count_frequencies(input_words))



# Problem 2: Intermediate Level
# Task: Write a function group_by_age(people) that takes a list of dictionaries containing people's names and ages, and returns a dictionary grouping names by their age.

# example inputs
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 25},
#     {"name": "David", "age": 30}
# ]

def group_by_age(people):
    pass


people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 25},
    {"name": "David", "age": 30}
]
print(group_by_age(people))