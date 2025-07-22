from aviation.fleet import (
    average_flight_length,
    passengers_per_day,
    required_global_fleet,
)

test_values = zip(
    [365_000_000_000.0, 2 * 366_000_000_000.0],  # passengers_per_year
    [365.0, 366.0],  # days_per_year
    [1_000_000_000.0, 2_000_000_000.0],  # expected_passengers_per_day
    strict=True,
)

for passengers_per_year, days_per_year, expected_passengers_per_day in test_values:
    passengers_per_day_result = passengers_per_day(passengers_per_year, days_per_year)
    assert passengers_per_day_result == expected_passengers_per_day, (
        f"{passengers_per_day_result=} != {expected_passengers_per_day=}"
    )

seats_per_aircraft = 250.0
flights_per_day = 3.0
expected_required_global_fleet = 1_000_000_000.0
required_global_fleet_result = required_global_fleet(
    passengers_per_day_result, seats_per_aircraft, flights_per_day
)
assert required_global_fleet_result == expected_required_global_fleet, (
    f"{required_global_fleet_result=} != {expected_required_global_fleet=}"
)

global_rpk_per_year = 1_000_000_000.0
passengers_per_year = 1_000_000_000.0
expected_average_flight_length = 1.0
average_flight_length_result = average_flight_length(global_rpk_per_year, passengers_per_year)
assert average_flight_length_result == expected_average_flight_length, (
    f"{average_flight_length_result=} != {expected_average_flight_length=}"
)
