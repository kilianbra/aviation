days_per_year = 366.0
passengers_per_year = 5.0e9
global_rpk_per_year = 9.0e12

aircraft_flights_per_day = 3.0
seats_per_aircraft = 250.0

passengers_per_day = passengers_per_year / days_per_year
required_global_fleet = passengers_per_day / (seats_per_aircraft * aircraft_flights_per_day)

print(f"Required global fleet: {required_global_fleet=:.0f} aircraft")

average_flight_length = global_rpk_per_year / passengers_per_year
print(f"Average flight length: {average_flight_length=:.0f} km")






