# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
diff_age = 90 - int(age)
age_in_days = diff_age * 365
age_in_weeks = diff_age * 52
age_in_months = diff_age * 12
print(f"You have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left.")
