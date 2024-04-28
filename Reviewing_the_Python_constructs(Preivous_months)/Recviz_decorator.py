'''
Implement the @recviz decorator, which fully visualizes the execution of the function being decorated, including
recursive ones. The decorator must display all recursive calls and the return values produced by those calls,
with depth-first recursive calls separated by four spaces.

The next call to the decorated function during visualization must include the -> sign, the name of the decorated
function and the arguments passed during this call. The return value when rendered must include the <- sign and the
return value itself.

Note 1: The recursive call and the return value obtained from that call must be at the same indentation level.

Note 2: Don't forget that the decorator should not consume the return value of the function being decorated, and should
also be able to decorate functions with an arbitrary number of positional and named arguments.
'''

import functools

def recviz(func):
    n = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal n
        arg_str = ', '.join(map(repr, args))
        kwarg_str = ', '.join(f"{key}={value!r}" for key, value in kwargs.items())
        arg_list = [arg_str]
        if kwarg_str:
            arg_list.append(kwarg_str)
        args_str = ', '.join(arg_list)
        prefix = "    " * n
        print(f"{prefix}-> {func.__name__}({args_str})")
        n +=1
        result = func(*args, **kwargs)
        print(f"{prefix}<- {result!r}")
        n-=1
        return result
    return wrapper

# Example
@recviz
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


fact(5)

# Output:
# -> fact(5)
#     -> fact(4)
#         -> fact(3)
#             -> fact(2)
#                 -> fact(1)
#                     -> fact(0)
#                     <- 1
#                 <- 1
#             <- 2
#         <- 6
#     <- 24
# <- 120