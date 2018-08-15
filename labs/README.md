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

7. Write a Python program to clone or copy a list.

8. Write a Python script to sort (ascending and descending) a dictionary by value.

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
