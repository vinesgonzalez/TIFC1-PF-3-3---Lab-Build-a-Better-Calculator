def main():
    print("Hello learners!")

    nums_list = [2, 3, 4]

    print("Sum:", addmultiplenumbers(nums_list))
    print("Multiplication:", multiplymultiplenumbers(nums_list))

    number = 4

    print("Is it even?", isiteven(number))
    print("Is it an integer?", isitaninteger(number))


def addmultiplenumbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def isiteven(num):
    return num % 2 == 0 and num == int(num)


def isitaninteger(num):
    return num == int(num)


if __name__ == "__main__":
    main()