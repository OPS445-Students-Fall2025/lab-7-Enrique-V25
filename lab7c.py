#!/usr/bin/env python3
# Student ID: emolina3
from lab7a import Time

def time_to_sec(t):
    """Convert a Time object to seconds"""
    return t.hour*3600 + t.minute*60 + t.second

def sec_to_time(seconds):
    """Convert seconds to a Time object"""
    seconds %= 24*3600
    h, remainder = divmod(seconds, 3600)
    m, s = divmod(remainder, 60)
    return Time(h, m, s)

def format_time(t):
    """Return time object (t) as a formatted string HH:MM:SS."""
    return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}"
