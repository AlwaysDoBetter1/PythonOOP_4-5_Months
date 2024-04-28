'''
Implement a @jsonify decorator that converts the return value of the function being decorated into a JSON formatted string.

The decorator must also store the name and docstring of the function being decorated.

Note 1: The function's return value is guaranteed to be of a type that is supported by the JSON format.
'''

import json
from functools import wraps

def jsonify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapper

# Example
@jsonify
def make_user(id, live, options):
    return {'id': id, 'live': live, 'options': options}


print(make_user(4, False, None))

# Output:
# {"id": 4, "live": false, "options": null}