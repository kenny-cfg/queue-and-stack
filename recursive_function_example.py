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


# Function that
#  * take a string
#  * returns True if it's a palindrome
#  * returns False otherwise


if __name__ == "__main__":
    result = sum_up_to(6) # 1 + 2 + 3 + 4 + 5 + 6
    print(result) # 21
    result = product_up_to(6) # 1 * 2 * 3 * 4 * 5 * 6
    print(result) # 720