"""Growth in global demand for aviation."""

__all__ = (
    "DemandGrowthModel",
    "demand_growth_model",
    "demand_growth_rate",
    "passengers_per_year",
)

import enum
import typing

import camia_model as model
from camia_model.units import DIMENSIONLESS, Quantity, percent, year

from aviation.units import passenger

PASSENGERS_PER_YEAR_IN_2025 = 5.0e9 * passenger / year


@enum.unique
class DemandGrowthModel(enum.Enum):
    """Different models that can be used for demand growth."""

    EXPONENTIAL = enum.auto()
    LINEAR = enum.auto()
    CONSTANT = enum.auto()


@model.transform
def demand_growth_model() -> DemandGrowthModel:
    """The default model that will be used for demand growth."""
    return DemandGrowthModel.EXPONENTIAL


@model.transform
def demand_growth_rate(
    demand_growth_model: DemandGrowthModel,
) -> typing.Annotated[Quantity, percent / year]:
    """Annual growth rate in percent per year."""
    match demand_growth_model:
        case DemandGrowthModel.EXPONENTIAL:
            return 4.0 * percent / year
        case DemandGrowthModel.LINEAR:
            return 1.0 * percent / year
        case DemandGrowthModel.CONSTANT:
            msg = "Constant demand has no growth rate."
            raise ValueError(msg)


@model.transform.switch(demand_growth_model=DemandGrowthModel.EXPONENTIAL)
def passengers_per_year(
    modelling_year: int,
    demand_growth_rate: typing.Annotated[Quantity, percent / year],
) -> typing.Annotated[Quantity, passenger / year]:
    """Calculate annual aviation passengers given a growth rate.

    Args:
        modelling_year: The year for which to calculate passenger demand.
        demand_growth_rate: Annual growth rate in percent per year.

    Returns:
        The number of passengers per year, as a Quantity with units passenger/year.
    """
    passengers_per_year_in_2025 = PASSENGERS_PER_YEAR_IN_2025
    growth_factor = (100.0 * percent + demand_growth_rate * 1.0 * year).convert_to(DIMENSIONLESS)

    return passengers_per_year_in_2025 * growth_factor ** (modelling_year - 2025)


@model.transform.switch(demand_growth_model=DemandGrowthModel.LINEAR)  # type: ignore[no-redef]
def passengers_per_year(  # noqa: F811
    modelling_year: int,
    demand_growth_rate: typing.Annotated[Quantity, percent / year],
) -> typing.Annotated[Quantity, passenger / year]:
    """Calculate annual aviation passengers given a growth rate.

    Args:
        modelling_year: The year for which to calculate passenger demand.
        demand_growth_rate: Annual growth rate in percent per year.

    Returns:
        The number of passengers per year, as a Quantity with units passenger/year.
    """
    passengers_per_year_in_2025 = PASSENGERS_PER_YEAR_IN_2025
    years_since_2025 = float(modelling_year - 2025) * year
    growth_factor = (100.0 * percent + demand_growth_rate * years_since_2025).convert_to(
        DIMENSIONLESS
    )

    return passengers_per_year_in_2025 * growth_factor


@model.transform.switch(demand_growth_model=DemandGrowthModel.CONSTANT)  # type: ignore[no-redef]
def passengers_per_year() -> typing.Annotated[Quantity, passenger / year]:  # noqa: F811
    """Calculate constant annual aviation passengers."""
    return PASSENGERS_PER_YEAR_IN_2025
