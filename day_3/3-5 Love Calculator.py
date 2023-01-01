# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
joined_name = name1.lower() + name2.lower()

true_dict = {}
love_dict = {}

true_string = "true"
love_string = "love"

for letter in true_string:
    true_dict.update({letter: joined_name.count(letter)})
for letter in love_string:
    love_dict.update({letter: joined_name.count(letter)})


score = int(str(sum(true_dict.values())) + str(sum((love_dict.values()))))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")