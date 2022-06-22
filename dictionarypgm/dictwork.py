car={"name":"swift","color":"grey","make":"2015","brand":"maruthi","fuel":"petrol","price":"9la","num_airbags":1}

print(car["brand"])
print(car["color"])
print(car["make"])
print(car["fuel"])
print("transmission_type" in car)
car["transmission_type"]="manual"
print(car)
print("break_type" in car)
car["break_type"]="abs"
print(car)
car["num_airbags"]=2
print(car)