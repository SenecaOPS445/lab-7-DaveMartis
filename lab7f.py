#!/usr/bin/env python3
# Student ID: [seneca_id]

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        """Return time object (t) as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum as a new Time object."""
        self_seconds = self.time_to_sec()
        t2_seconds = t2.time_to_sec()
        total_seconds = self_seconds + t2_seconds
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Change the time object by adding or subtracting seconds."""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour = new_time.hour
        self.minute = new_time.minute
        self.second = new_time.second

    def time_to_sec(self):
        """Convert the time object to a single integer representing the number of seconds from midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

    def __str__(self):
        """Return a string representation of the time object."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation for the object."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """Add two Time objects and return the sum as a new Time object."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

def sec_to_time(seconds):
    """Convert a given number of seconds to a Time object in hour, minute, second format."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

# Testing the Time class and its methods in an interactive Python shell
if __name__ == "__main__":
    t1 = Time(9, 50, 0)
    t2 = Time(1, 1, 1)
    print(t1.sum_times(t2))  # Should print 10.51.01
    print(t2.sum_times(t1))  # Should print 10.51.01
    print(t1 + t2)  # Should print 10.51.01
    x = t1 + t2
    print(type(x))  # Should print <class 'lab7f.Time'>
    print(x)  # Should print 10:51:01



