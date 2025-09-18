import math

def lcm(x, y):

    if x == y:
        return x

    return abs(x * y) // math.gcd(x, y)

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def main():
    print("LCM Calculator")

    x = get_positive_integer("Enter a value for x: ")
    y = get_positive_integer("Enter a value for y: ")

    result = lcm(x, y)

    print(f"The LCM of {x} and {y} is = {result}")

if __name__ == "__main__":
    main()



