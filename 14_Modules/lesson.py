"""Import standard-library modules and a project-local helper."""
from datetime import date
import math
import random

from helpers import greet

print(greet("Sam"))
print(f"pi={math.pi:.3f}; die roll={random.randint(1, 6)}; today={date.today():%Y-%m-%d}")
