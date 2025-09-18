def isPalindrome(valStr):
    """Check if a string is palindrome."""
    return valStr == valStr[::-1]


def toBinaryIfNumber(value):
    """Convert to binary if input is numeric."""
    if value.isdigit():
        return bin(int(value))[2:]
    return None

def main():
    value = input("Enter a value: ")

    input_palindrome = isPalindrome(value)
    print("Input is a palindrome:", input_palindrome)

    binary_val = toBinaryIfNumber(value)

    if binary_val:
        print("Binary equivalent:", binary_val)
        binary_palindrome = isPalindrome(binary_val)
        print("Binary is a palindrome:", binary_palindrome)
    else:
        print("(No binary conversion since input is text)")

if __name__ == "__main__":
    main()
