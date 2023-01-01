# Day 9-2 Dictionaries in Lists - write a function that updates a list of
# dictionaries with a new dictionary containing travel information.
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

# We can simply append a new dictionary to travel_log, with the function
# arguments as dict values.
def add_new_country(country, times_visited, cities):
    travel_log.append({"country": country, "visits": times_visited, "cities": cities})

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
