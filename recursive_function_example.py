def sum_up_to(upper_limit):
    sum = 0
    for i in range(upper_limit + 1):
        sum += i
    return sum


if __name__ == "__main__":
    result = sum_up_to(6) # 1 + 2 + 3 + 4 + 5 + 6
    print(result) # 21