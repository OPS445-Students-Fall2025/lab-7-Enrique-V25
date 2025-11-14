#!/usr/bin/env python3
# Student ID: emolina3

class Time:
    """Simple object type for time of the day"""
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def time_to_sec(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def change_time(self, seconds):
        """Change internal time by adding seconds"""
        total = self.time_to_sec() + seconds
        new_t = sec_to_time(total)
        self.hour, self.minute, self.second = new_t.hour, new_t.minute, new_t.second


def sec_to_time(seconds):
    """Convert seconds → Time object"""
    seconds %= 86400  # wrap at 24 hours
    h = seconds // 3600
    seconds %= 3600
    m = seconds // 60
    s = seconds % 60
    return Time(h, m, s)


# REQUIRED by CheckLab7.py
def format_time(t):
    """Wrapper for Time.format_time"""
    return t.format_time()


# REQUIRED by CheckLab7.py
def change_time(t, seconds):
    """Wrapper for Time.change_time"""
    t.change_time(seconds)
    return None

