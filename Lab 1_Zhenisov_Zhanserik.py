import numpy as np

# 1)Write a program to hold a small database of food items and their costs using two lists.
food_items = []
food_costs = []


def add_food_item(item, cost):
    food_items.append(item)
    food_costs.append(cost)
    print(f"Added {item} with a cost of ${cost:.2f}")


add_food_item('milk', 1)


# 2)Create a 2D array of zero integers,
# fill with some numbers and print out the full array then print out some slices from the array.

array = np.zeros((3, 4), dtype=int)

array[0] = [1, 2, 3, 4]
array[1] = [5, 6, 7, 8]
array[2] = [9, 10, 11, 12]

# Print the full array
print("Full Array:")
print(array)

# 3)Create a list with the names of 10 'friends'. Create a second matching list with their years of birth.

friends = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6', 'Name7', 'Name8', 'Name9', 'Name10']
years_of_birth = [2005, 2004, 2006, 2005, 2004, 2004, 2003, 2001, 2000, 2007]

for i in range(len(friends)):
    print(f"{friends[i]} was born in {years_of_birth[i]}.")

# Ex1 You have to read a statement of the 1st exercise(Lists) and write a program with a dictionary.
food_database = {}


def add_food_item(item, cost):
    food_database[item] = cost
    print(f"Added {item} with a cost of ${cost:.2f}")


add_food_item('milk', 1.15)

# Ex2 Try to execute problem of 10 'friends'

friends_birth_years = {}


def add_friends(friends, years_of_birth):
    for i in range(len(friends)):
        friends_birth_years[friends[i]] = years_of_birth[i]  # Map each friend to their year of birth


add_friends(friends, years_of_birth)


print(friends_birth_years)

# (Ex1) Formulate and output an array with the size N (you choose), that consists of N odd numbers


def generate_odd_numbers(n):
    odd_numbers = [2 * i + 1 for i in range(n)]
    return odd_numbers


n = 10
odd_numbers_array = generate_odd_numbers(n)
print(odd_numbers_array)


# (Ex2) Let be given N(you choose), and the first member A and difference D of arithmetic progression/sequence.
# Output the first N numbers of that sequence
N = 10
n_seq = []


def arithmetic_progression(a, d, n):
    for i in range(n):
        term = a + i * d
        n_seq.append(term)


arithmetic_progression(1, 1, N)

print(n_seq)

# (Ex3) Let be given N(you choose), and the first member A and difference D of geometric progression/sequence.
# Output the first N numbers of that sequence
n_seq_of_geom = []


def geometric_progression(a, d, n):
    for i in range(n):
        term = a * (d ** i)
        n_seq_of_geom.append(term)


geometric_progression(1, 2, N)

print(n_seq_of_geom)

# (Ex4)Let be given N(you choose).
# Output an array of the size N that contains first N elements of Fibonnacci numbers

first_num = 0
second_num = 1
Fib_seq = [first_num, second_num]

for i in range(2, N):
    next_num = first_num + second_num
    Fib_seq.append(next_num)
    first_num = second_num
    second_num = next_num

print(Fib_seq)

# (Ex5) Let be given N(you choose but greater than 2), A and B.
# Write a program to output an array of the size N, first element of which is equal to A,
# the second - to B, and each subsequent element is equal to the sum of all the previous ones.
List_of_arr = []


def sum_arr(a, b, N):
    List_of_arr.append(a)
    List_of_arr.append(b)
    for i in range(2, N):
        next_num = sum(List_of_arr)
        List_of_arr.append(next_num)


sum_arr(1, 2, N)
print(List_of_arr)

