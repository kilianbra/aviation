import pytest

from aviation.fleet import (
    average_flight_length,
    passengers_per_day,
    required_global_fleet,
)


@pytest.mark.parametrize(
    ("passengers_per_year", "days_per_year", "expected_passengers_per_day"),
    (
        (365_000_000.0, 365.0, 1_000_000.0),
        (2 * 366_000_000.0, 366.0, 2_000_000.0),
    ),
)
def test_passengers_per_day(
    passengers_per_year: float,
    days_per_year: float,
    expected_passengers_per_day: float,
) -> None:
    assert passengers_per_day(passengers_per_year, days_per_year) == expected_passengers_per_day


@pytest.mark.parametrize(
    ("passengers_per_year", "seats_per_aircraft", "flights_per_aircraft_per_day"),
    (
        (5_000_000_000.0, 250.0, 3.0),
        (4_000_000_000.0, 200.0, 3.0),
    ),
)
def test_required_global_fleet(
    passengers_per_year: float,
    seats_per_aircraft: float,
    flights_per_aircraft_per_day: float,
) -> None:
    days_per_year = 365.0
    expected_required_global_fleet = 25_000.0

    passengers_per_day_result = passengers_per_day(passengers_per_year, days_per_year)

    result = required_global_fleet(
        passengers_per_day_result,
        seats_per_aircraft,
        flights_per_aircraft_per_day,
    )
    tolerance = 10_000.0
    assert result == pytest.approx(expected_required_global_fleet, abs=tolerance)


def test_average_flight_length() -> None:
    global_rpk_per_year = 9_000_000_000_000.0
    passengers_per_year = 5_000_000_000.0
    expected_average_flight_length = 2_000.0

    result = average_flight_length(global_rpk_per_year, passengers_per_year)
    tolerance_relative = 0.1
    assert result == pytest.approx(expected_average_flight_length, rel=tolerance_relative)
