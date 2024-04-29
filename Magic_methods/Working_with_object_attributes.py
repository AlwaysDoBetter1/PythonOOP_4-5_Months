'''
We will consider an attribute to be protected if its name begins with an underscore (_). For example, _password, __email
and __dict__.

Implement the ProtectedObject class. When instantiated, the class must accept an arbitrary number of named arguments.
All arguments passed must be set as attributes to the instance being created.

The ProtectedObject class must prohibit obtaining or changing the values of protected attributes of its instances, as
well as deleting these attributes or creating new ones. When attempting to get or change the value of a protected
attribute, or attempting to delete an attribute or create a new one, an AttributeError exception must be raised
with the text:

Protected attribute cannot be accessed
Note 1. Additional data verification for correctness is not required. It is guaranteed that the implemented class
is used only with correct data.
'''


class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __delattr__(self, attr):
        if attr[0] == "_":
            raise AttributeError("Access to a protected attribute is not allowed")
        object.__delattr__(self, attr)

    def __setattr__(self, key, val):
        if key.startswith("_"):
            raise AttributeError("Access to a protected attribute is not allowed")
        super().__setattr__(key, val)

    def __getattribute__(self, val):
        if val.startswith("_"):
            raise AttributeError("Access to a protected attribute is not allowed")
        return object.__getattribute__(self, val)

# Example:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)

# Output:
# PG_kamiya
# Access to a protected attribute is not allowed
