import typing

import camia_engine as engine
import pytest
import pytest_camia
from camia_model.units import Quantity, day, year

import aviation
from aviation.units import aircraft, journey, passenger


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        (
            {"passengers_per_year": 5_000_000_000.0 * passenger / year},
            "passengers_per_year",
            5_000_000_000.0 * passenger / year,
        ),
        (
            {"required_global_fleet": 25_000.0 * aircraft},
            "required_global_fleet",
            25_000.0 * aircraft,
        ),
        (
            {
                "passengers_per_year": 5_000_000_000.0 * passenger / year,
            },
            "passengers_per_day",
            13_689_253.0 * passenger / day,
        ),
        (
            {
                "passengers_per_day": 13_689_253.0 * passenger / day,
                "seats_per_aircraft": 200.0 * passenger / aircraft,
                "flights_per_aircraft_per_day": 3.0 * journey / (day * aircraft),
            },
            "required_global_fleet",
            22_815.0 * aircraft,
        ),
        (
            {
                "passengers_per_year": 10_000_000_000.0 * passenger / year,
                "seats_per_aircraft": 200.0 * passenger / aircraft,
                "flights_per_aircraft_per_day": 3.0 * journey / (day * aircraft),
            },
            "required_global_fleet",
            2 * 22_815.0 * aircraft,
        ),
    ),
)
def test_systems_model_evaluate(
    systems_model: engine.SystemsModel,
    inputs: dict[str, typing.Annotated[Quantity, float]],
    output: str,
    expected: typing.Annotated[Quantity, float],
) -> None:
    assert systems_model.evaluate(inputs, output) == pytest_camia.approx(expected, atol=1.0)
