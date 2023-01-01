# Day 2 Project: Calculate tip per person based on partysize, bill total,
# and tipping percentage

print("Welcome to the Python tip calculator!")
party_size = int(input("How many people are splitting the bill? "))
bill_total = int(input("What is the bill total? "))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15%? "))
# cauculating bill per person and printing a two-decimal string representation
bill_per_person = (bill_total / party_size) * (1 + (tip_percent / 100))
rounded_bill = "{:.2f}".format(bill_per_person)
print(f"Each person in the party should pay: {rounded_bill}")
