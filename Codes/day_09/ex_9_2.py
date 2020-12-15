

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

def add_new_country(add_country, add_visits, add_cities):
    temp_d = {}
    temp_d["country"] = add_country
    temp_d["visits"] = add_visits
    temp_d["cities"] = add_cities
    # travel_log.append(temp_d.copy()) # .copy()
    travel_log.append(temp_d)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



