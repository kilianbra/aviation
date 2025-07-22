"""This module contains functions for calculating the required global aviation aircraft fleet.

The functions are:
    passengers_per_day: Calculate the global number of aviation passengers per day.
    required_global_fleet: Calculate the required global aviation aircraft fleet.
    average_flight_length: Calculate the average flight length.
"""


def passengers_per_day(passengers_per_year, days_per_year):
    """Calculate the global number of aviation passengers per day.

    A passenger is a person flying at one point, so if one person flies twice (return flight) in a given year, this will
        count as two passengers.

    Args:
        passengers_per_year (float): The total number of passengers flying per year.
        days_per_year (float): The number of days in the year.

    Returns:
        passengers_per_day (float): The number of passengers per day.
    """
    return passengers_per_year / days_per_year


def required_global_fleet(passengers_per_day, seats_per_aircraft, aircraft_flights_per_day):
    """Calculate the required global aviation aircraft fleet.

    Args:
        passengers_per_day (float): The number of passengers per day.
        seats_per_aircraft (float): The number of seats per aircraft.
        aircraft_flights_per_day (float): The number of flights per aircraft per day.

    Returns:
        required_global_fleet (float): The required global aviation aircraft fleet.
    """
    return passengers_per_day / (seats_per_aircraft * aircraft_flights_per_day)


def average_flight_length(global_rpk_per_year, passengers_per_year):
    """Calculate the average flight length.

    Args:
        global_rpk_per_year (float): The total number of RPK per year.
        passengers_per_year (float): The total number of passengers per year.

    Returns:
        average_flight_length (float): The average flight length.
    """
    return global_rpk_per_year / passengers_per_year
