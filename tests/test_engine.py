import pytest

import aviation
from aviation import _engine as engine


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        ({"passengers_per_year": 5_000_000_000}, "passengers_per_year", 5_000_000_000),
        ({"required_global_fleet": 25_000}, "required_global_fleet", 25_000),
        (
            {
                "passengers_per_year": 5_000_000_000,
                "days_per_year": 365.25,
            },
            "passengers_per_day",
            13_689_253,
        ),
        (
            {
                "passengers_per_day": 13_689_253,
                "seats_per_aircraft": 200,
                "aircraft_flights_per_day": 3,
            },
            "required_global_fleet",
            22_815,
        ),
        (
            {
                "passengers_per_year": 10_000_000_000,
                "days_per_year": 365.25,
                "seats_per_aircraft": 200,
                "aircraft_flights_per_day": 3,
            },
            "required_global_fleet",
            2 * 22_815,
        ),
    ),
)
def test_systems_model_evaluate(
    systems_model: engine.SystemsModel,
    inputs: dict[str, float],
    output: str,
    expected: float,
) -> None:
    assert systems_model.evaluate(inputs, output) == pytest.approx(expected, abs=1.0)
