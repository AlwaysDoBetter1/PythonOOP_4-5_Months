'''
Contextlib Example
'''

from contextlib import ExitStack

def print_this(*args):
    print(*args)

with ExitStack() as stack:
    stack.callback(print_this, 'bee')
    stack.callback(print_this, 'bee', 'geek')
    stack.close()
    stack.callback(print_this, 'b', 'e', 'e')
    stack.close()

# Output:
# bee geek
# bee
# b e e