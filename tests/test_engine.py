import camia_engine as engine
import pytest

import aviation


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        ({"passengers_per_year": 5_000_000_000.0}, "passengers_per_year", 5_000_000_000.0),
        ({"required_global_fleet": 25_000.0}, "required_global_fleet", 25_000.0),
        (
            {
                "passengers_per_year": 5_000_000_000.0,
                "days_per_year": 365.25,
            },
            "passengers_per_day",
            13_689_253,
        ),
        (
            {
                "passengers_per_day": 13_689_253.0,
                "seats_per_aircraft": 200.0,
                "aircraft_flights_per_day": 3.0,
            },
            "required_global_fleet",
            22_815.0,
        ),
        (
            {
                "passengers_per_year": 10_000_000_000.0,
                "days_per_year": 365.25,
                "seats_per_aircraft": 200.0,
                "aircraft_flights_per_day": 3.0,
            },
            "required_global_fleet",
            2 * 22_815.0,
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
