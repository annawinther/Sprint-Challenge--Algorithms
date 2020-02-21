#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
    a = 0 
    while (a < n * n * n): 
      a = a + n * n  
```

b)
```
    sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

c)
```
     def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II


