"""
Various enumerations used throughout the program 
"""

import enum from Enum

class HealthStatus(Enum):
    healthy = 1
    unhealthy = 2
    dead = 3

class DecisionType(Enum):
    good = 1
    bad = 2
    neutral = 3
