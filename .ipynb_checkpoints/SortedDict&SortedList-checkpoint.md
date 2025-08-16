```python
# Import the sorted containers library
from sortedcontainers import SortedList, SortedDict

# Create a sorted list with some values
sl = SortedList(['e', 'a', 'c', 'd', 'b'])
print(sl) # SortedList(['a', 'b', 'c', 'd', 'e'])

# Add a new value to the sorted list
sl.add('f')
print(sl) # SortedList(['a', 'b', 'c', 'd', 'e', 'f'])

# Find the index of a value in the sorted list
print(sl.bisect_left('c')) # 2

# Create a sorted dict with some items
sd = SortedDict({'c': -3, 'a': 1, 'b': 2})
print(sd) # SortedDict({'a': 1, 'b': 2, 'c': -3})

# Set a new item in the sorted dict
sd['d'] = 4
print(sd) # SortedDict({'a': 1, 'b': 2, 'c': -3, 'd': 4})

# Get an item by index in the sorted dict
print(sd.iloc[0]) # ('a', 1)

# Get a slice of items in the sorted dict
print(sd.irange('b', 'd')) # ['b', 'c', 'd']
```