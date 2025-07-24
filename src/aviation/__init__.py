"""This module contains functions for calculating the required global aviation aircraft fleet.

Modules:
    fleet: Contains functions for calculating the required global aviation aircraft fleet.

Functions:
    passengers_per_day: Calculate the global number of aviation passengers per day.
    required_global_fleet: Calculate the required global aviation aircraft fleet.
    average_flight_length: Calculate the average flight length.
"""

__all__ = ("DemandGrowthModel", "transforms")

from aviation.demand import (
    DemandGrowthModel,
    demand_growth_model,
    demand_growth_rate,
    passengers_per_year,
)
from aviation.fleet import (
    average_flight_length,
    passengers_per_day,
    required_global_fleet,
)  # the first aviation is the folder (package)name, the second is the file (module) name

transforms = (
    passengers_per_day,
    required_global_fleet,
    average_flight_length,
    passengers_per_year,
    demand_growth_rate,
    demand_growth_model,
)
