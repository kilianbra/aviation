"""This analysis uses transforms for calculating the passengers per year."""

import camia_engine as engine
from camia_model.units import percent, year

import aviation

# Parameters
start_year = 2025
num_years = 26
demand_growth_rate = 1.0 * percent / year  # Example growth rate

total_passengers = 0.0
final_year_value = None

systems_model = engine.SystemsModel(aviation.transforms)
output = "passengers_per_year"

for i in range(num_years):
    current_year = start_year + i
    inputs = {
        "modelling_year": current_year,
        "demand_growth_rate": demand_growth_rate,
    }
    passengers_per_year = systems_model.evaluate(inputs, output)
    total_passengers += passengers_per_year.value
    if i == num_years - 1:
        final_year_passengers = passengers_per_year

print(f"Total passengers over {num_years} years: {total_passengers:.3e}")
print(
    f"Passengers in final year ({start_year + num_years - 1}): {final_year_passengers.value:,.0f} "
    f"{final_year_passengers.unit}"
)
