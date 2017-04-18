def generate_prime_numbers(number=None):
    prime_nums = []
    if not number:
        raise ValueError("Please enter a parameter")
    elif type(number) == int:
        for num in range(1, number):
            if all(num % i != 0 for i in range(2, num)):
                prime_nums.append(num)

        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    return prime_nums
            else:
                prime_nums.append(number)
    else:
        raise ValueError("The provided input value is not an integer.")

    return prime_nums
