# Python Data Structures Workshop Solutions

## String

1. Write a function that takes a character (i.e. a string of length 1) and returns `True` if it is a vowel, `False` otherwise.

[Solution](../sy_bsc_it/solution_1.py)

2. Write a function that takes a string and prints count of letters and digits in that string.

[Solution](string_solution_2.py)

3. Write a function that checks if a string is palindrome. E.g. 

```python
>>> msg = "Step on no pets"
>>> is_palindrome(msg)
True
```

[Solution](../sy_bsc_it/solution_3.py)

## List

1. Write a function that takes a list as input and returns a new list with first and last element of input list.

```python
>>> input = [10, 20, 30, 40, 50]
>>> get_new_list(input)
[10, 50]
```

[Solution](list_solution_1.py)

2. Write a function to flatten a nested list.

```python
>>> input = [['A','B'],['C','D'],['E','F']]
>>> my_flat_list_fn(input)
['A', 'B', 'C', 'D', 'E', 'F']
```

[Solution](list_solution_2.py)


3. Write a function that takes a word and a character as input and returns a list with index positions of the character in the word.

```python
>>> my_char_index_fn("mississippi", "s")
[2, 3, 5, 6]
```

[Solution](list_solution_3.py)

4. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
<br/>&#42;&#42;&#42;&#42; <br/>
&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42;&#42; <br/>
&#42;&#42;&#42;&#42;&#42;&#42;&#42; <br/>

[Solution](../sy_bsc_it/solution_2.py)

## Tuple

1. Write a program to swap values of two variables without using a third variable.

**Solution:**

```python
a = 10
b = 20
a, b = b, a
```

2. Create a tuple with a single element "A".

**Solution:**

```python
t = ('A',)
```

3. Predict the output and tell me WHY?

```python
>>> x = 10
>>> y = 20
>>> x, y = y, x+y
```

**Solution:**

```
>>> x = 10
>>> y = 20
>>> x, y = y, x+y
>>> x
20
>>> y
30
```

Reason is tuple packing and unpacking.

## Set

1. Write a functions that takes a word returns consonants in that word.

```python
>>> word="Independence"
>>> get_consonants(word)
{'c', 'd', 'p', 'n'}
```

[Solution](set_solution_1.py)

2. Write a function that takes two lists and returns True if they have at least one common member, False otherwise.

[Solution](../sy_bsc_it/solution_5.py)

3. A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.
 
[Solution](../sy_bsc_it/solution_3.py)


## Dictionary

1. Write a program to print following dictionary in 
* Lexical order of Country Name
* Descending order of Country Name length

```python
>>> capitals = {'India': 'Delhi', 'Bangladesh': 'Dhaka', 'England': 'London', 'Canada': 'Ottawa'}
```

[Solution](dict_solution_1.py)

2. Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :  

```python
dic1 = { 1: 10, 2: 20 } 
dic2 = { 3: 30, 4: 40 } 
dic3 = { 4: 50, 5: 60 }
```
 
Expected Result : 

```python
{ 1: 10, 2: 20, 3: 30, 4: 50, 5: 60 }
```

**Solution:**


```python
>>> dic1 = { 1: 10, 2: 20 } 
>>> dic2 = { 3: 30, 4: 40 } 
>>> dic3 = { 4: 50, 5: 60 }
>>> dic4 = dic1.copy()
>>> dic4.update(dic2)
>>> dic4.update(dic3)
>>> dic4
{1: 10, 2: 20, 3: 30, 4: 50, 5: 60}
```
