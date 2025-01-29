from enum import Enum

class Vehicle(Enum):
    TWO_WHEEL = 1
    COMPACT_4_WHEEL = 2
    LARGE_4_WHEEL = 3
    HEAVY_DUTY_BUS = 4

def get_cost(vehicle, time):
    if vehicle == Vehicle.TWO_WHEEL:
        return 5*time
    elif vehicle == Vehicle.COMPACT_4_WHEEL:
        return 7*time
    elif vehicle == Vehicle.LARGE_4_WHEEL:
        return 9*time
    elif vehicle == Vehicle.HEAVY_DUTY_BUS:
        return 11*time
