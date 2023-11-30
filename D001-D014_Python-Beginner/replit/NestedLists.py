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

def add_new_country(country_visited, num_of_visits, city_visited):
    new_country = {
        "country":country_visited,
        "visits":num_of_visits,
        "cities":city_visited
    }
    travel_log.append({new_country})

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)