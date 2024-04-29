'''
Just example enter and exit operators
'''


class ContextManager:
    def __init__(self):
        self.inside = False

    def __enter__(self):
        self.inside = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.inside = False
        return True


context = ContextManager()
print(context.inside)

with context:
    print(context.inside)

print(context.inside)

# Output:
# False
# True
# False