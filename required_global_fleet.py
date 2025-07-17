import aviation

passengers_per_year = 5.0e9
flights_per_day = 3.0
seats_per_aircraft = 250.0
days_per_year = 366.0

passengers_per_day = aviation.passengers_per_day(passengers_per_year, days_per_year)
required_global_fleet = aviation.required_global_fleet(passengers_per_day, seats_per_aircraft, flights_per_day)

print(f"Required global fleet: {required_global_fleet=:.0f} aircraft")





