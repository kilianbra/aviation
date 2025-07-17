import aviation

global_rpk_per_year = 9.0e12
passengers_per_year = 5.0e9

average_flight_length = aviation.average_flight_length(global_rpk_per_year, passengers_per_year)
print(f"Average flight length: {average_flight_length=:,.0f} km")
