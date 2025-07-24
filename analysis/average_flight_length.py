"""This module contains functions for calculating the average flight length."""

import camia_engine as engine
from camia_model.units import kilometer, year

import aviation
from aviation.units import journey, passenger

global_rpk_per_year = 9.0e12 * passenger * kilometer / year / journey
passengers_per_year = 5.0e9 * passenger / year

inputs = {
    "global_rpk_per_year": global_rpk_per_year,
    "passengers_per_year": passengers_per_year,
}

output = "average_flight_length"

systems_model = engine.SystemsModel(aviation.transforms)
average_flight_length = systems_model.evaluate(inputs, output)
print(f"Average flight length: {average_flight_length.value=:,.0f} {average_flight_length.unit}")
