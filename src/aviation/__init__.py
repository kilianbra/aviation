__all__ = [
    "required_global_fleet",
    "passengers_per_day",
    "average_flight_length",
]  # Makes them imported when import * but also important for general code working


from aviation.fleet import (
    average_flight_length,
    passengers_per_day,
    required_global_fleet,
)
# the first aviation is the folder name, the second is the file name
# this represents the package name and the module

# Now we have added the functions in the fleet module to the package namespace
# This means we can now import the functions directly from the package namespace with
# the import in __init__.py. Here are the different ways to import and use functions:
#
# 1. import aviation
#    aviation.fleet.passengers_per_day()
#    aviation.passengers_per_day()
#
# 2. from aviation import fleet
#    fleet.passengers_per_day()
#
# 3. from aviation import passengers_per_day
#    passengers_per_day()
#
# 4. from aviation.fleet import passengers_per_day
#    passengers_per_day()
