"""This module contains functions for calculating the passengers per day."""

import camia_engine as engine
from camia_model.units import day, year

import aviation
from aviation.units import passenger

days_per_year = 365.25 * day / year
passengers_per_year = 5.0e9 * passenger / year

inputs = {
    "passengers_per_year": passengers_per_year,
}

output = "passengers_per_day"

systems_model = engine.SystemsModel(aviation.transforms)
passengers_per_day = systems_model.evaluate(inputs, output)
print(f"Passengers per day: {passengers_per_day.value=:,.0f} {passengers_per_day.unit}")
