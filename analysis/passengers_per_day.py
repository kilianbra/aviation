from aviation import fleet

days_per_year = 366.0
passengers_per_year = 5.0e9

passengers_per_day = fleet.passengers_per_day(passengers_per_year, days_per_year)
print(f"Passengers per day: {passengers_per_day=:,.0f}")
