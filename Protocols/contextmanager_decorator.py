'''
Implement the safe_write context manager using the @contextmanager decorator, which takes one argument:

filename - file name
The context manager must allow information to be written to a file named filename. Moreover, if any exception
was thrown while writing to a file, the context manager must absorb it, cancel all previously executed
writes to the file, if any, return the file to its original state and inform about the thrown exception by
outputting the following text:
An exception <exception type> was thrown while writing to the file.
'''

from contextlib import contextmanager
import io
import sys

@contextmanager
def safe_write(filename):
    flag = True
    exc = None
    try:
        buffer = io.StringIO()
        sys.stdout = buffer
        yield buffer
    except Exception as e:
        exc = type(e).__name__
        flag = False
    finally:
        sys.stdout = sys.__stdout__
        if flag:
            with open(filename, "w") as f:
                f.write(buffer.getvalue())
        else:
            print(f"An exception was thrown while writing to the file {exc}")

# Example
with safe_write('under_tale.txt') as file:
    file.write('The shadow of ruins looms over you, filling you with determination\n')

with safe_write('under_tale.txt') as file:
    print('Under the merry rustle of leaves, you fill with determination', file=file)
    raise ValueError

with open('under_tale.txt') as file:
    print(file.read())

# Output:
# A ValueError exception was thrown while writing to the file
# The shadow of the ruins looms over you, filling you with determination