'''
Python is memory managed language but for working with files required closing operators, greatest operator is 'with'
'''

with open('output.txt', mode='w', encoding='utf-8') as file:
    print(file.closed)

print(file.closed)

# Output:
# False
# True