# Python Data Structures Workshop Solutions

## String

1. Write a function that takes a character (i.e. a string of length 1) and returns "Vowel" if it is a vowel, "Consonant" otherwise.

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

## Dictionary


