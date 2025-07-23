"""This module contains functions for calculating the passengers per day."""

import camia_engine as engine

import aviation

days_per_year = 366.0
passengers_per_year = 5.0e9

inputs = {
    "passengers_per_year": passengers_per_year,
    "days_per_year": days_per_year,
}

output = "passengers_per_day"

systems_model = engine.SystemsModel(aviation.transforms)
passengers_per_day = systems_model.evaluate(inputs, output)
print(f"Passengers per day: {passengers_per_day=:,.0f}")
