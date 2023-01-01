# Day 5-3 Adding Even Numbers: Write a script that returns the sum of all
# even numbers between 1-100, inclusive.

#Write your code below this row 👇

# We can simply use range() starting at 0, and incrementing by 2.
# This will only include even numbers. (0 + 2 = 2, 2 + 2 = 4, etc.)
# You can also use increment of 1 and do a modulo check to determine evens.
sum_even_numbers = sum(range(0, 101, 2))
print(sum_even_numbers)
