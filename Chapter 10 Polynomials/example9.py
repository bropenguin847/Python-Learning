"""
Chapter 10 Example 9
This is a continuation of example 4. It imports from stability_check.py
in the same folder

Stable:     All real parts of the roots are negative.
Not Stable: Any root has a real part that is zero or positive.
"""

from stability_check import chk_stable

# Example usage:
chk_stable([4, 1, 0], [1], [1, -2])       # Example system
chk_stable([1, 1, 2], [1], [1, -2])       # Example system
chk_stable([3, 3, 3], [1, 0], [1, 1])     # Example system
