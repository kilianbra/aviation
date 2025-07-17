def passengers_per_day(passengers_per_year, days_per_year):
    return passengers_per_year / days_per_year


def required_global_fleet(
    passengers_per_day, seats_per_aircraft, aircraft_flights_per_day
):
    return passengers_per_day / (seats_per_aircraft * aircraft_flights_per_day)


def average_flight_length(global_rpk_per_year, passengers_per_year):
    return global_rpk_per_year / passengers_per_year
