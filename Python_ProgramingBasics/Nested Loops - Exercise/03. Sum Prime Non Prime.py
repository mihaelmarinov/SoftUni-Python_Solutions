command = input()

prime_num = 0
non_prime_num = 0

while command != "stop":

    number = int(command)
    if number < 0:
        print("Number is negative.")
        pass

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                non_prime_num += number
                break
        else:
            prime_num += number


    command = input()

print(f"Sum of all prime numbers is: {prime_num}")
print(f"Sum of all non prime numbers is: {non_prime_num}")
