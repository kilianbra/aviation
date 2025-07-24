"""This module contains functions for calculating the required global aviation aircraft fleet.

The functions are:
    passengers_per_day: Calculate the global number of aviation passengers per day.
    required_global_fleet: Calculate the required global aviation aircraft fleet.
    average_flight_length: Calculate the average flight length.
"""

import typing

import camia_model as model
from camia_model.units import Quantity, day, kilometer, year

from aviation.units import aircraft, journey, passenger


@model.transform
def passengers_per_day(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
) -> typing.Annotated[Quantity, passenger / day]:
    """Calculate the global number of aviation passengers per day.

    A passenger is a person flying at one point, so if one person flies twice (return flight)
    in a given year, this will count as two passengers.

    Args:
        passengers_per_year: The total number of passengers flying per year.
        days_per_year: The number of days in the year.

    Returns:
        passengers_per_day: The number of passengers per day.
    """
    return passengers_per_year.convert_to(passenger / day)


@model.transform
def required_global_fleet(
    passengers_per_day: typing.Annotated[Quantity, passenger / day],
    seats_per_aircraft: typing.Annotated[Quantity, passenger / (aircraft)],
    flights_per_aircraft_per_day: typing.Annotated[Quantity, journey / (day * aircraft)],
) -> typing.Annotated[Quantity, aircraft]:
    """Calculate the required global aviation aircraft fleet.

    Args:
        passengers_per_day: The number of passengers per day.
        seats_per_aircraft: The number of seats per aircraft.
        flights_per_aircraft_per_day: The number of flights per aircraft per day.

    Returns:
        required_global_fleet: The required global aviation aircraft fleet.
    """
    aircraft_per_journey = 1.0 * aircraft / journey
    return passengers_per_day / (
        seats_per_aircraft * flights_per_aircraft_per_day * aircraft_per_journey
    )


@model.transform
def average_flight_length(
    global_rpk_per_year: typing.Annotated[Quantity, passenger * kilometer / year / journey],
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
) -> typing.Annotated[Quantity, kilometer / journey]:
    """Calculate the average flight length.

    Args:
        global_rpk_per_year: The total number of RPK per year.
        passengers_per_year: The total number of passengers per year.

    Returns:
        average_flight_length: The average flight length.
    """
    return global_rpk_per_year / passengers_per_year
