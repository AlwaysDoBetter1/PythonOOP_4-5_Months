'''
Implement a generator function annual_return() that takes three arguments in the following order:

start — integer, initial deposit amount in rubles
percent — integer, the percentage by which the current deposit amount will increase every year
years — integer, number of years during which interest will accrue
The function should return an iterator simulating a bank deposit. The return values of the iterator should be the size
of the deposit after the next calculation of percent.
'''

def annual_return(start, percent, years):
    for i in range(years):
        start = start + start * percent/100
        yield start

for value in annual_return(70000, 8, 10):
    print(round(value))

# Output:
# 75600
# 81648
# 88180
# 95234
# 102853
# 111081
# 119968
# 129565
# 139930
# 151125