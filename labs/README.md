1. Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise. 

[Solution](solution_1.py)

2. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
<br/>&#42;&#42;&#42;&#42; <br/>
&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42; <br/>
&#42;&#42;&#42;&#42;&#42;&#42;&#42; <br/>

[Solution](solution_2.py)

3. A  pangram is a sentence that contains all the letters of the English alphabet at least once, for example: 
**The quick brown fox jumps over the lazy dog** . 
Your task here is to write a function to check a sentence to see if it is a pangram or not.

[Solution](solution_3.py)

4. Take a list, say for example this one:

```python
a=[1,1,2,3,5,8,13,  21,  34,  55,  89]   
```

and write a program that prints out all the elements of the list that are less than 5.

[Solution](solution_4.py)

5. Write a program that takes two lists and returns True if they have at least one common member.

[Solution](solution_5.py)

6. Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.

**Solution:**

```python
>>> my_list = [0,1,2,3,4,5,6,7,8,9]
>>> my_list = my_list[1:2]+my_list[3:4]+my_list[6:]
>>> my_list
[1, 3, 6, 7, 8, 9]
```

Note: Following can **not** be a solution.

```python
>>> my_list = [0,1,2,3,4,5,6,7,8,9]
>>> del my_list[0]
>>> del my_list[2]
>>> del my_list[4]
>>> del my_list[5]
>>> my_list
[1, 2, 4, 5, 7, 9]
```

7. Write a Python program to clone or copy a list.

**Solution:**

```python
>>> l1 = [1,2,3]
>>> l2 = l1[:]			# Shallow Copy
>>> import copy
>>> l2 = copy.copy(l1)		# Shallow Copy
>>> l2 =  copy.deepcopy(l1)	# Deep Copy
```

[Click Here for detailed example](solution_7.md)

8. Write a Python script to sort (ascending and descending) a dictionary by value.

**Solution:**

```python
>>> d = dict(a=12,b=21,c=3,d=19,e=11,f=7,g=12)

>>> sorted(d.items(),key=lambda val:val[1])   					# Ascending by values 
[('c', 3), ('f', 7), ('e', 11), ('a', 12), ('g', 12), ('d', 19), ('b', 21)]

>>> sorted(d.items(),key=lambda val:val[1], reverse=True)			# Descending by values
[('b', 21), ('d', 19), ('a', 12), ('g', 12), ('e', 11), ('f', 7), ('c', 3)]
```

9. Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :  

```python
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
```
 
Expected Result : 

```python
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
```

**Solution:**

```python
>>> dic1={1:10, 2:20} 
>>> dic2={3:30, 4:40} 
>>> dic3={5:50,6:60} 
>>> dic4=dic1.copy()
>>> dic4.update(dic2)
>>> dic4.update(dic3)
>>> dic4
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
```

10. Write a Python program to sum all the items in a dictionary.

**Solution**:

```python
>>> d = dict(a=12,b=21,c=3,d=19,e=11,f=7,g=12)
>>> sum(d.values())
85
```

Caveat: Here the assumption is values in the dictionary are of same type (int, float, str, list) and sum can be performed on them.
