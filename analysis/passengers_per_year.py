"""This analysis uses transforms for calculating the passengers per year."""

import camia_engine as engine
from camia_model.units import percent, year

import aviation

# Parameters
years = list(range(2025, 2051))
num_years = 26
demand_growth_rate = 4.0 * percent / year  # Example growth rate

total_passengers = 0.0
final_year_value = None

systems_model = engine.SystemsModel(aviation.transforms)
output = "passengers_per_year"

inputs = {
    "modelling_year": years,
    "demand_growth_rate": demand_growth_rate,
}
passengers_per_year = systems_model.evaluate(inputs, output)

list_result = [
    f"In year {year}: {k.value:>15,.0f} {k.unit} \n"
    for year, k in zip(
        passengers_per_year.coords["modelling_year"].values, passengers_per_year.values, strict=True
    )
]
print("".join(list_result))
