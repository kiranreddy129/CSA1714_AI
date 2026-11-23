outlook = input("Enter weather (sunny/rainy): ")
wind = input("Enter wind (strong/weak): ")

if outlook == "sunny":
    result = "No"
elif outlook == "rainy":
    if wind == "strong":
        result = "No"
    else:
        result = "Yes"
else:
    result = "Invalid input"

print("Play Cricket:", result)
