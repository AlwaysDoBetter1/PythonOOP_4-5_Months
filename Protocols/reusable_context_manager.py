'''
Implement the AdvancedTimer class. When presenting an example class, you should not accept any arguments.

An instance of the AdvancedTimer class should be a reusable context manager that measures the execution time of the
code within each block.

Also, an instance of the AdvancedTimer class must have four attributes:

Last_run is a number indicating the execution time of the code inside the last block with
runs - a list of numbers, each of which represents the execution time of some code inside the block c. The first
element of the table must occupy this place during execution of the code inside the first c block, the second
element - inside the second c block, and so on.
min - a number representing the minimum execution time of the code inside the block among all measurements
max — a number showing the maximum execution time of the code inside the block among all measurements
If an instance of the AdvancedTimer class has never been used to measure the execution speed of any block code,
the values of the last_run, min, and max attributes must be None.
'''

import time

class AdvancedTimer:
    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        run_time = end_time - self.start_time

        self.last_run = run_time
        self.runs.append(run_time)

        if self.min is None or run_time < self.min:
            self.min = run_time

        if self.max is None or run_time > self.max:
            self.max = run_time

        return False
# Example
from time import sleep

timer = AdvancedTimer()
with timer:
    sleep(1.5)
print(round(timer.last_run, 1))
with timer:
    sleep(0.7)
print(round(timer.last_run, 1))
with timer:
    sleep(1)
print(round(timer.last_run, 1))

# Output:
# 1.5
# 0.7
# 1.0