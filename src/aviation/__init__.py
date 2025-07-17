__all__ = ["required_global_fleet", "passengers_per_day", "average_flight_length"] # Makes them imported when import *


from aviation.fleet import required_global_fleet, passengers_per_day, average_flight_length
# the first aviation is the folder name, the second is the file name
# this represents the package name and the module

# Now we have added the functions in the fleet module to the package namespace
# This means we can now import the functions directly from the package namespace (thanks to the import in __init__.py)
# so we can import aviation and then use aviation.fleet.passengers_per_day(passengers_per_year, days_per_year)
# or can directly call aviation.passengers_per_day(passengers_per_year, days_per_year)
# We can also from aviation import fleet and then use fleet.passengers_per_day(passengers_per_year, days_per_year)
# or from aviation import passengers_per_day and then use passengers_per_day(passengers_per_year, days_per_year)
# or finally from aviation.fleet import passengers_per_day and then use passengers_per_day(passengers_per_year, days_per_year)
# (this would have been required if we hadn't added the functions to the package namespace thanks to the import in __init__.py
