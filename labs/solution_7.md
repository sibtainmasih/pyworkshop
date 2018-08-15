```python
>>> l1 = [1,2,3]
>>> l2 = l1
>>> l1 == l2
True
>>> l2.append(4)
>>> l1
[1, 2, 3, 4]
>>> l1 is l2
True
>>> l3 = l1[:]		# Shallow Copy
>>> l3.append(5)
>>> l1
[1, 2, 3, 4]
>>> l3
[1, 2, 3, 4, 5]
>>> l1 is l3
False

>>> new_l = ["A",l1]
>>> new_l
['A', [1, 2, 3, 4]]
>>> import copy
>>> new_l2 = copy.copy(new_l)		# Shallow Copy
>>> new_l2.append('B')
>>> new_l
['A', [1, 2, 3, 4]]
>>> new_l2
['A', [1, 2, 3, 4], 'B']
>>> new_l is new_l2
False
>>> l1.append(5)
>>> l1
[1, 2, 3, 4, 5]
>>> new_l
['A', [1, 2, 3, 4, 5]]
>>> new_l2
['A', [1, 2, 3, 4, 5], 'B']
>>> new_l3 =  copy.deepcopy(new_l)	# Deep Copy
>>> l1.append(6)
>>> l1
[1, 2, 3, 4, 5, 6]
>>> new_l
['A', [1, 2, 3, 4, 5, 6]]
>>> new_l2
['A', [1, 2, 3, 4, 5, 6], 'B']
>>> new_l3
['A', [1, 2, 3, 4, 5]]
```
