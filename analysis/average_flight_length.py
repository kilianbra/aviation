"""This module contains functions for calculating the average flight length."""

import camia_engine as engine

import aviation

global_rpk_per_year = 9.0e12
passengers_per_year = 5.0e9

inputs = {
    "global_rpk_per_year": global_rpk_per_year,
    "passengers_per_year": passengers_per_year,
}

output = "average_flight_length"

systems_model = engine.SystemsModel(aviation.transforms)
average_flight_length = systems_model.evaluate(inputs, output)
print(f"Average flight length: {average_flight_length=:,.0f} km")
