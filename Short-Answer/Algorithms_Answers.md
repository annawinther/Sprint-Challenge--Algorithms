#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
    a = 0 # O(1)
    while (a < n * n * n): #O(1) * O(n) 
      a = a + n * n  # O(1)
      # O(1) + O(n) + O(1) 
      # = O(n)
```
This is O(n) becasue the while loop run until a < n^3. It will increase by n^2 and as the input size increases the runtime grows at the same rate. 


b)
```python
    sum = 0 # O(1)
    for i in range(n): # O(n) * O(n) = O(n^2)
      j = 1 # O(1)
      while j < n: # O(1) * O(n)
        j *= 2 # O(1)
        sum += 1
```
This has a runtime complexity of O(n^2). As the size ofo the input increases, the runtime will grow at a faser rate. 

c)
```python
     def bunnyEars(bunnies): 
      if bunnies == 0: # O(1)
        return 0 

      return 2 + bunnyEars(bunnies-1) # O(n)
```
This is a recursive function and everytime we're looping over it the n is decremented by 1. This therefore has a runtime of O(n)

## Exercise II


