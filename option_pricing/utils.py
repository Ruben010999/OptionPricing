"""
Utility functions shared across the project.
"""

def annualize_days(days: int) -> float:
    """
    Convert days to year fraction using 365-day convention.
    """
    return days / 365.0
