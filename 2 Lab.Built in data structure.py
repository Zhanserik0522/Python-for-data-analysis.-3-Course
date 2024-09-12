# Ex1
def multiply_fractions(frac1, frac2):
    num = frac1[0] * frac2[0]
    denom = frac1[1] * frac2[1]
    return num, denom


def divide_fractions(frac1, frac2):
    num = frac1[0] * frac2[1]
    denom = frac1[1] * frac2[0]
    return num, denom


def find_smallest_fraction(fractions):
    smallest = fractions[0]
    for frac in fractions[1:]:
        if frac[0] * smallest[1] < smallest[0] * frac[1]:
            smallest = frac
    return smallest


def +(fraction_str):
    numerator, denominator = map(int, fraction_str.split('/'))
    return numerator, denominator


def main():
    print("== Multiplication and Division ==")
    frac1 = parse_fraction(input("Enter a fraction >>> "))
    frac2 = parse_fraction(input("Enter a fraction >>> "))

    product = multiply_fractions(frac1, frac2)
    quotient = divide_fractions(frac1, frac2)

    print(f"Multiplication of the fractions: {product[0]}/{product[1]}")
    print(f"Division of the first by the second: {quotient[0]}/{quotient[1]}")

    print("== Smallest fraction ==")
    fractions = []

    while True:
        fraction_str = input("Enter a fraction >>> ")
        if fraction_str.lower() == "stop":
            break
        fractions.append(parse_fraction(fraction_str))

    if fractions:
        smallest = find_smallest_fraction(fractions)
        print(f"Smallest fraction: {smallest[0]}/{smallest[1]}")
    else:
        print("No fractions entered.")


# if __name__ == "__main__":
#     main()


# Ex 2

def just_list(numbers):
    return numbers, sum(numbers) / len(numbers), sum(numbers)


def list_with_even(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return evens, sum(evens) / len(evens) if evens else 0, sum(evens)


def list_with_odd(numbers):
    odds = [num for num in numbers if num % 2 != 0]
    return odds, sum(odds) / len(odds) if odds else 0, sum(odds)


def main_2():
    numbers = []

    while True:
        input_str = input("Input a number >>> ")
        if input_str.lower() == "stop":
            break
        try:
            number = int(input_str)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid integer.")

    all_nums, avg_all, sum_all = just_list(numbers)

    evens, avg_even, sum_even = list_with_even(numbers)

    odds, avg_odd, sum_odd = list_with_odd(numbers)

    print(f"All numbers: {all_nums}")
    print(f"Average of all numbers: {avg_all}")
    print(f"Sum of all numbers: {sum_all}")

    print(f"Even numbers: {evens}")
    print(f"Average of even numbers: {avg_even}")
    print(f"Sum of even numbers: {sum_even}")

    print(f"Odd numbers: {odds}")
    print(f"Average of odd numbers: {avg_odd}")
    print(f"Sum of odd numbers: {sum_odd}")


# if __name__ == "__main__":
#     main_2()

# Ex 3


def insert_in_order(sorted_list, num):
    for i in range(len(sorted_list)):
        if num == sorted_list[i]:
            return
        elif num < sorted_list[i]:
            sorted_list.insert(i, num)
            return

    sorted_list.append(num)


def main3():
    sorted_list = []
    while True:
        input_str = input("Input a number >>> ")
        if input_str.lower() == "stop":
            break
        try:
            num = float(input_str)
            insert_in_order(sorted_list, num)
            print(f'List contains {sorted_list}')
        except ValueError:
            print("Please enter a valid number.")

    print(f'Final sorted list: {sorted_list}')


# if __name__ == "__main__":
#     main3()

# Option 1
# Task 1, 2, 3

def nums_of_pos(my_list):
    count = 0
    for num in my_list:
        if num > 0:
            count += 1
    return count


def largest(my_list):
    largest = my_list[0]
    index_of_lar_num = 0

    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]
            index_of_lar_num = i

    return largest, index_of_lar_num


def smallest_odd(my_list):
    new_list_of_odd = [x for x in my_list if x % 2 != 0]
    smallest = new_list_of_odd[0]

    if len(new_list_of_odd) == 0:
        return 0

    for num in new_list_of_odd:
        if num < smallest:
            smallest = num

    return smallest

def main4():
    my_list = [7, -1, -2, 0, -1, 2, -1, 6]

    ans = nums_of_pos(my_list)
    largest_value, largest_index = largest(my_list)
    smallest = smallest_odd(my_list)
    print(f"The number of positive (>0) items in this list is equal to {ans}")
    print(f"The largest value in the list is {largest_value}")
    print(f"The index of the largest value is {largest_index}")
    print(f"The smallest value in the list is {smallest}")

if __name__ == "__main__":
    main4()