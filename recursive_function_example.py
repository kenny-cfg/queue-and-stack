# Recursion
# * Starting point (typically, i = 0, or empty string, or empty collection
# * Code to reduce any other value to a smaller value (typically,
#   reduce the argument, or a shorter string, or a smaller collection

def sum_up_to(upper_limit):
    if upper_limit == 0:
        return 0
    return upper_limit + sum_up_to(upper_limit - 1)

# Write a function that multiplies all the numbers up to the one supplied


def product_up_to(upper_limit):
    if upper_limit == 1:
        return 1
    return upper_limit * product_up_to(upper_limit - 1)


def is_palindrome(source):
    if len(source) <= 1:
        return True
    last_letter = source[-1]
    first_letter = source[0]
    if last_letter != first_letter:
        return False
    remainder = source[1:-1]
    return is_palindrome(remainder)

# Function that
#  * take a string
#  * returns True if it's a palindrome
#  * returns False otherwise
# ABBA is a palindrome
# racecar is a palindrome


if __name__ == "__main__":
    result = is_palindrome('racecar')
    print(result)
    result = is_palindrome('fireworks')
    print(result)