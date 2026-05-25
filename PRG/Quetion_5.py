# Question 5 - Taxi Fare Calculator

# List of trips with distance (km) and hour of travel (24hr format)
trips = [
    {'distance': 1.5,  'hour': 14},
    {'distance': 5.0,  'hour': 22},
    {'distance': 12.0, 'hour': 3},
    {'distance': 8.5,  'hour': 10},
    {'distance': 2.0,  'hour': 23},
]

# Go through each trip and calculate the fare
for trip in trips:
    distance = trip['distance']
    hour     = trip['hour']
    fare     = 0

    # Validate: distance must be positive and hour must be 0-23
    if distance <= 0:
        print('Invalid distance for trip:', trip)
        continue   # Skip this trip and go to the next one

    if hour < 0 or hour > 23:
        print('Invalid hour for trip:', trip)
        continue   # Skip this trip and go to the next one

    # First 2 km costs a flat NPR 150 base fare
    if distance <= 2:
        fare = 150

    # Between 2 km and 10 km: base + NPR 35 per extra km
    elif distance <= 10:
        extra_km = distance - 2
        fare = 150 + (extra_km * 35)

    # Beyond 10 km: add NPR 28 per km on top of the 10 km cost
    else:
        fare = 150 + (8 * 35)          # Cost for the first 10 km
        extra_km = distance - 10
        fare = fare + (extra_km * 28)  # Add cost beyond 10 km

    # Night surcharge: 10% extra if travelling between 10 PM and 5 AM
    if hour >= 22 or hour < 5:
        fare = fare + (fare * 10 / 100)

    # Print the result for this trip
    print('Distance:', distance, 'km | Hour:', hour,
          '| Fare: NPR', round(fare, 2))
