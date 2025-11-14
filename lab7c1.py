# lab7c.py

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_sec(self):
        """Convert this Time object to total seconds."""
        return self.hour * 3600 + self.minute * 60 + self.second

    @staticmethod
    def sec_to_time(total_seconds):
        """Convert seconds into a Time object."""
        hour = total_seconds // 3600
        minute = (total_seconds % 3600) // 60
        second = total_seconds % 60
        return Time(hour, minute, second)

    def add(self, other):
        """Return a new Time object that is the sum of two times."""
        total_seconds = self.time_to_sec() + other.time_to_sec()
        return Time.sec_to_time(total_seconds)

    def sub(self, other):
        """Return a new Time object that is the difference between two times."""
        total_seconds = self.time_to_sec() - other.time_to_sec()
        if total_seconds < 0:
            total_seconds = 0
        return Time.sec_to_time(total_seconds)

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

def time_to_sec(t):
    """Convert a Time object to seconds."""
    return t.hour * 3600 + t.minute * 60 + t.second


def sec_to_time(total_seconds):
    """Convert seconds to a Time object."""
    hour = total_seconds // 3600
    minute = (total_seconds % 3600) // 60
    second = total_seconds % 60
    return Time(hour, minute, second)


def sum_times(t1, t2):
    """Return a new Time object equal to t1 + t2."""
    total = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total)


def change_time(t, seconds):
    """Add or subtract seconds from a Time object and return a new Time."""
    total = time_to_sec(t) + seconds
    if total < 0:
        total = 0
    return sec_to_time(total)

