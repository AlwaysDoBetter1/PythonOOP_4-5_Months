'''
Example of hashable objects
'''


hashes = set()

for _ in range(100):
    hashes.add(hash('beegeek'))

print(len(hashes))

# Output:
# 1