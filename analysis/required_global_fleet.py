"""This module contains functions for calculating the required global fleet."""

import aviation
from aviation import _engine as engine

passengers_per_year = 5.0e9
flights_per_aircraft_per_day = 3.0
seats_per_aircraft = 250.0
days_per_year = 366.0

inputs = {
    "passengers_per_year": passengers_per_year,
    "flights_per_aircraft_per_day": flights_per_aircraft_per_day,
    "seats_per_aircraft": seats_per_aircraft,
    "days_per_year": days_per_year,
}

output = "required_global_fleet"

systems_model = engine.SystemsModel(aviation.transforms)
required_global_fleet = systems_model.evaluate(inputs, output)

print(f"Required global fleet: {required_global_fleet=:,.0f} aircraft")
