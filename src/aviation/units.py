"""Additional units to support accurate unit annotations of transforms."""

import camia_model as model

passenger = model.units.Unit.new_named("passenger", relation=model.units.DIMENSIONLESS)
aircraft = model.units.Unit.new_named("aircraft", relation=model.units.DIMENSIONLESS)
journey = model.units.Unit.new_named("journey", relation=model.units.DIMENSIONLESS)
