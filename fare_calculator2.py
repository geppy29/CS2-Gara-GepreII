# Travel Fare Calculator
FARE_RATE = 14

# Validate passenger name
while True:
    name = input("Enter passenger name: ")
    if name.strip() != "":
        break  # Stops loop once name is entered.
    else:
        print("Error: Invalid! Name cannot be empty.")

# Validate distance
while True:
    distance_str = input("Enter distance (km): ")
    try:
        distance = float(distance_str)
        if distance > 0:
            break  # Stops loop once a valid distance is entered.
        else:
            print("Error: Invalid! Enter a number greater than 0.")
    except ValueError:
        print("Error: Invalid! Enter a valid number for distance.")

# Validate number of passengers
while True:
    passengers_str = input("Enter number of passengers: ")
    if passengers_str.isdigit():
        passengers = int(passengers_str)
        if passengers > 0:
            break  # Stops loop once valid number of passengers is entered.
        else:
            print("Error: Invalid! Enter a number greater than 0.")
    else:
        print("Error: Invalid! Enter a whole positive number.")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
