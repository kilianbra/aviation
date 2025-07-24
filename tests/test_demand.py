import typing

import pytest
import pytest_camia
from camia_model.units import Quantity, percent, year

from aviation.demand import DemandGrowthModel, demand_growth_rate, passengers_per_year
from aviation.units import passenger


def test_demand_growth_rate() -> None:
    assert demand_growth_rate(DemandGrowthModel.EXPONENTIAL) == pytest_camia.approx(
        4.0 * percent / year
    )
    assert demand_growth_rate(DemandGrowthModel.LINEAR) == pytest_camia.approx(1.0 * percent / year)
    with pytest.raises(ValueError, match="Constant demand has no growth rate."):
        demand_growth_rate(DemandGrowthModel.CONSTANT)


@pytest.mark.parametrize(
    (
        "modelling_year",
        "demand_growth_rate",
        "expected_passengers_per_year",
    ),
    (
        (2025, 4.0 * percent / year, 5.0e9 * passenger / year),
        (2025, 1.0 * percent / year, 5.0e9 * passenger / year),
        (2050, 4.0 * percent / year, 13_329_181_657.0 * passenger / year),
        (2050, 1.0 * percent / year, 6_412_159_975.0 * passenger / year),
    ),
)
def test_passengers_per_year(
    modelling_year: int,
    demand_growth_rate: typing.Annotated[Quantity, percent / year],
    expected_passengers_per_year: typing.Annotated[Quantity, passenger / year],
) -> None:
    with passengers_per_year.context(demand_growth_model=DemandGrowthModel.EXPONENTIAL):
        assert passengers_per_year(
            modelling_year=modelling_year, demand_growth_rate=demand_growth_rate
        ) == pytest_camia.approx(expected_passengers_per_year)
