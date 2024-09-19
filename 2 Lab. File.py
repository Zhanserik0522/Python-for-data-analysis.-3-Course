import os

# Ex 1
# Write a program that takes in a filename,
# then takes in a series of lines of input until a blank line is entered, writing each line to the file with
# the given name. After the blank line is entered, properly close the file before ending the program.


def main1():
    name_of_file = input('Write the name of the file: ')

    with open(name_of_file, 'a') as file:
        while True:
            input_str = input('Enter your string (blank line to stop): ')

            if input_str.strip() == '':
                break

            file.write(input_str + '\n')

    print(f'Content written to {name_of_file}')


# Ex 2
# Write a program that takes in a filename and string as input.
# Then print how many times that string appears inside the chosen file. If the file
# does not exist, continue asking for a filename until one is given that exists.
# Use your source code file as test input.


def main2():
    while True:
        name_of_file = input('Write the name of the file: ')
        if os.path.isfile(name_of_file):
            break
        else:
            print(f"File '{name_of_file}' does not exist. Please enter a valid file name.")

    search_str = input('Write the string that needs to be checked: ')

    count = 0

    with open(name_of_file, 'r') as file:
        for line in file:
            count += line.count(search_str)

    print(f"The string '{search_str}' appears {count} times in the file '{name_of_file}'.")


# Option 1
# Task 1. The input file contains two integers, each on a separate line.
# Output their sum to the output file.

def main3():
    with open('Task1','r') as file:
        ans = 0
        for line in file:
            ans += int(line.strip())

    print(f"The sum of int is equal to {ans}")


# Task 2. The input file contains a single text string, possibly containing spaces.
# Print this line in reverse order. The line in the input file ends
# with the end of line character '\n'.

def main4():
    with open("Task2", "r") as file:
        ans = file.read().strip()

    print(ans[::-1])


if __name__ == "__main__":
    choice = input("Which main function do you want to run? (1 , 2 , 3 , 4): ")
    if choice == "1":
        main1()
    elif choice == "2":
        main2()
    elif choice == "3":
        main3()
    elif choice == "4":
        main4()
    else:
        print("Invalid choice. Exiting.")