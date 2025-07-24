import typing

import pytest
import pytest_camia
from camia_model.units import Quantity, day, kilometer, year

from aviation.fleet import (
    average_flight_length,
    passengers_per_day,
    required_global_fleet,
)
from aviation.units import aircraft, journey, passenger


@pytest.mark.parametrize(
    ("passengers_per_year", "expected_passengers_per_day"),
    (
        (365_250_000.0 * passenger / year, 1_000_000.0 * passenger / day),
        (2 * 365_250_000.0 * passenger / year, 2_000_000.0 * passenger / day),
    ),
)
def test_passengers_per_day(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
    expected_passengers_per_day: typing.Annotated[Quantity, passenger / day],
) -> None:
    assert passengers_per_day(passengers_per_year) == pytest_camia.approx(
        expected_passengers_per_day
    )


@pytest.mark.parametrize(
    ("passengers_per_year", "seats_per_aircraft", "flights_per_aircraft_per_day"),
    (
        (
            5_000_000_000.0 * passenger / year,
            250.0 * passenger / aircraft,
            3.0 * journey / (day * aircraft),
        ),
        (
            4_000_000_000.0 * passenger / year,
            200.0 * passenger / aircraft,
            3.0 * journey / (day * aircraft),
        ),
    ),
)
def test_required_global_fleet(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
    seats_per_aircraft: typing.Annotated[Quantity, passenger / aircraft],
    flights_per_aircraft_per_day: typing.Annotated[Quantity, journey / (day * aircraft)],
) -> None:
    expected_required_global_fleet = 25_000.0 * aircraft

    passengers_per_day_result = passengers_per_day(passengers_per_year)

    result = required_global_fleet(
        passengers_per_day=passengers_per_day_result,
        seats_per_aircraft=seats_per_aircraft,
        flights_per_aircraft_per_day=flights_per_aircraft_per_day,
    )
    tolerance = 10_000.0
    assert result == pytest_camia.approx(expected_required_global_fleet, atol=tolerance)


def test_average_flight_length() -> None:
    global_rpk_per_year = 9_000_000_000_000.0 * passenger * kilometer / year / journey
    passengers_per_year = 5_000_000_000.0 * passenger / year
    expected_average_flight_length = 2_000.0 * kilometer / journey

    result = average_flight_length(global_rpk_per_year, passengers_per_year)
    tolerance_relative = 0.15
    assert result == pytest_camia.approx(expected_average_flight_length, rtol=tolerance_relative)
