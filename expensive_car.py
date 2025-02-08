# random_names= ["James", "Jack", "Jacob", "Josh", "Jake", "Jason"]
# for name in random_names:
#   print(name)

random_car_info =[
  {
    "make": "Toyota",
    "model": "Camry",
    "year": "2020",
    "pricing": "30000"
  },
  {
    "make": "Honda",
    "model": "Civic",
    "year": "2020",
    "pricing": "20000"
  },
  {
    "make": "Ford",
    "model": "F150",
    "year": "2020",
    "pricing": "40000"
  },
  {
    "make": "Chevy",
    "model": "Silverado",
    "year": "2020",
    "pricing" : "35000"
  }
]

random_car_info.append(
  {
    "make": "Tesla",
    "model": "Model 3",
    "year": "2020",
    "pricing" : "65000"
  }
)
expensive_car = random_car_info[0]
print("avaiable cars in stock:")
for car in random_car_info:
  if int(expensive_car["pricing"]) < int(car["pricing"]):
    expensive_car = car
  print(car["make"])
print(f'most expensive car is {expensive_car["make"]} priced a {expensive_car["pricing"]}')
