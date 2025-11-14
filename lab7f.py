#!/usr/bin/env python3
# Student ID: emolina3
class Time:
    """Simple object type for time of the day with operator overloading"""
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __add__(self, other):
        """Overload + operator to sum two Time objects"""
        total_sec = self.time_to_sec() + other.time_to_sec()
        return sec_to_time(total_sec)

    def time_to_sec(self):
        return self.hour*3600 + self.minute*60 + self.second

def sec_to_time(seconds):
    seconds %= 24*3600
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return Time(h, m, s)
