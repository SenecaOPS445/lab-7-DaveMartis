#!/usr/bin/env python3
# Student ID: [seneca_id]

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def time_to_sec(time):
    """Convert a time object to a single integer representing the number of seconds from midnight."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object in hour, minute, second format."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    seconds_t1 = time_to_sec(t1)
    seconds_t2 = time_to_sec(t2)
    total_seconds = seconds_t1 + seconds_t2
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Change the given time object by adding or subtracting seconds."""
    total_seconds = time_to_sec(time) + seconds
    new_time = sec_to_time(total_seconds)
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second

# Uncomment the following lines if you want to test directly in this file
# if __name__ == "__main__":
#     t1 = Time(8, 0, 0)
#     t2 = Time(8, 55, 0)
#     t3 = Time(9, 50, 0)
#     td = Time(0, 50, 0)
#     tsum1 = sum_times(t1, td)
#     tsum2 = sum_times(t2, td)
#     change_time(t3, 1800)
#     print(format_time(t1), '+', format_time(td), '-->', format_time(tsum1))
#     print(format_time(t2), '+', format_time(td), '-->', format_time(tsum2))
#     print('09:50:00 + 1800 sec', '-->', format_time(t3))


