import math


def rectangle_area(height, width):
    return height * width


def rectangle_perimeter(height, width):
    return 2 * (height + width)


def rectangle_diagonal(height, width):
    return math.sqrt(height**2 + width**2)


def circle_area(radius):
    return math.pi * radius**2


def circle_circumference(radius):
    return 2 * math.pi * radius


def triangle_area(height, base):
    return 0.5 * height * base


def triangle_perimeter(height, base):
    hypotenuse = math.sqrt(height**2 + base**2)
    return height + base + hypotenuse


def polygon_exterior_angle(num_sides):
    return 360 / num_sides


def polygon_interior_angle(num_sides):
    return (num_sides - 2) * 180 / num_sides


def polygon_interior_angle_sum(num_sides):
    return (num_sides - 2) * 180


def polygon_area(num_sides, side_length):
    return (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))


def main():
    # Rectangle calculations
    height = float(input("Enter height of a rectangle >>> "))
    width = float(input("Enter width of a rectangle >>> "))
    print(f"The area of a rectangle with height {height} and width {width} is {rectangle_area(height, width):.2f}.")
    print(f"The perimeter of a rectangle with height {height} and width {width} is {rectangle_perimeter(height, width):.2f}.")
    print(f"The length of the diagonal of a rectangle with height {height} and width {width} is {rectangle_diagonal(height, width):.6f}.")

    # Circle calculations
    radius = float(input("Enter the radius of a circle >>> "))
    print(f"The area of a circle with radius {radius:.2f} is {circle_area(radius):.2f}.")
    print(f"The circumference of a circle with radius {radius:.2f} is {circle_circumference(radius):.2f}.")

    # Right triangle calculations
    triangle_height = float(input("Enter the height of a right triangle >>> "))
    triangle_base = float(input("Enter the base of a right triangle >>> "))
    print(f"The area of a right triangle with height {triangle_height:.2f} and base {triangle_base:.2f} is {triangle_area(triangle_height, triangle_base):.2f}.")
    print(f"The perimeter of a triangle with height {triangle_height:.2f} and base {triangle_base:.2f} is {triangle_perimeter(triangle_height, triangle_base):.2f}.")

    # Regular polygon calculations
    num_sides = int(input("Enter the number of sides of a regular polygon as >>> "))
    side_length = float(input("Enter the length of the side of a regular polygon >>> "))
    print(f"The exterior angle of a regular polygon with {num_sides} sides is {polygon_exterior_angle(num_sides):.2f} degrees.")
    print(f"The interior angles of a regular polygon with {num_sides} sides sum to {polygon_interior_angle_sum(num_sides):.2f} degrees.")
    print(f"Each interior angle of a regular polygon with {num_sides} sides is {polygon_interior_angle(num_sides):.2f} degrees.")
    print(f"The area of a regular polygon with {num_sides} sides each {side_length:.2f} long is {polygon_area(num_sides, side_length):.2f}.")


# if __name__ == "__main__":
#     main()


# Ex2
def calculate_actual_charge(charge):
    if charge < 10:
        return charge
    elif charge < 25:
        return charge + 3
    elif charge < 50:
        return charge + 8
    elif charge < 100:
        return charge + 20
    else:
        return charge + 25


# def main1():
#     charge = float(input("Enter value you want to charge >>> "))
#     actual_charge = calculate_actual_charge(charge)
#     print(f"{actual_charge:.2f} dollars were added to your calling card.")
#
#
# if __name__ == "__main__":
#     main1()


# Ex 3

def multiply(x, y):
    ans = 0
    while x > 0:
        if x % 2 == 1:
            ans += y
        x //= 2
        y *= 2
    return ans


def multiply_recursive(x, y):
    if x == 0:
        return 0
    if x % 2 == 0:
        return multiply_recursive(x // 2, y * 2)
    else:
        return y + multiply_recursive(x // 2, y * 2)


def main2():
    answer = multiply(8, 38)
    print(f"The result of 8 × 38 is {answer}")
    answer = multiply_recursive(8, 38)
    print(f"The result of 8 × 38 is {answer}")


if __name__ == "__main__":
    main2()