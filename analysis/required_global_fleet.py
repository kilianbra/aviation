"""This module contains functions for calculating the required global fleet."""

import camia_engine as engine
from camia_model.units import day, year

import aviation
from aviation.units import aircraft, journey, passenger

passengers_per_year = 5.0e9 * passenger / year
flights_per_aircraft_per_day = 3.0 * journey / (day * aircraft)
seats_per_aircraft = 250.0 * passenger / aircraft

inputs = {
    "passengers_per_year": passengers_per_year,
    "flights_per_aircraft_per_day": flights_per_aircraft_per_day,
    "seats_per_aircraft": seats_per_aircraft,
}

output = "required_global_fleet"

systems_model = engine.SystemsModel(aviation.transforms)
required_global_fleet = systems_model.evaluate(inputs, output)

print(f"Required global fleet: {required_global_fleet.value=:,.0f} {required_global_fleet.unit}")
print(f"{required_global_fleet}")
