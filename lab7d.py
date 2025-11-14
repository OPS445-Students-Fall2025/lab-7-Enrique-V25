#!/usr/bin/env python3
# Student ID: emolina3
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    function attributes: __init__, __str__, __repr__,
                         time_to_sec, format_time,
                         change_time, sum_times, valid_time
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum"""
        total_sec = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_sec)

    def change_time(self, seconds):
        """Add or subtract seconds from this time object"""
        total_sec = self.time_to_sec() + seconds
        t = sec_to_time(total_sec)
        self.hour, self.minute, self.second = t.hour, t.minute, t.second
        return None

    def time_to_sec(self):
        """Convert a time object to total seconds"""
        return self.hour*3600 + self.minute*60 + self.second

    def valid_time(self):
        """Check if time is valid"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True

def sec_to_time(seconds):
    """Convert seconds to a Time object"""
    seconds %= 24*3600  # wrap around 24 hours
    h, remainder = divmod(seconds, 3600)
    m, s = divmod(remainder, 60)
    return Time(h, m, s)

