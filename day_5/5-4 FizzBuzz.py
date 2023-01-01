# Day 5-4: Write a script goes through 1 - 100 and prints "Fizz" if a number
# is cleanly divisible by 3, "Buzz" if by 5, and "FizzBuzz" if by both.
# Print the number if the above doesn't apply.

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
