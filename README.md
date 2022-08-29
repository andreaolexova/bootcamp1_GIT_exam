# bootcamp1_GIT_exam
## Introduction
Repo bootcamp_GIT_exam is created as a part of exam in bootcamp I. internal workshop.

### repo structure
**I choose to work with some easy python code** in files:
- *moving_average.py* 
  - random lib
  - do moving/floating average
  - [click here for definition](https://www.geeksforgeeks.org/how-to-calculate-moving-averages-in-python/)
- ***prime_num.py***
  - work with bolean (flag) setup
  - user put num from command line first (not random func)

1. there are many branches for testing GIT options from bootcamp 1 exam
2. I already delete some of them :) 

![image](https://user-images.githubusercontent.com/110408006/187169910-c297eef0-1df0-47db-a952-fee1dc1ee640.png)

## RESULT code for moving average math
Note: you could allways run the code and get expected result.
```
# Given a series of numbers and a fixed subset size, the first element of the moving average is obtained by taking
# the average of the initial fixed subset of the number series. Then the subset is modified by "shifting forward";
# that is, excluding the first number of the series and including the next value in the subset.

# https://www.geeksforgeeks.org/how-to-calculate-moving-averages-in-python/

# Klouzavý průměr je: Statistická metoda eliminující výkyvy v časových řadách. Počítá se z údajů časové řady tak,
# že se postupně k danému počtu údajů (např. 12 měsíců) přiřazuje vždy jeden údaj následující a první údaj v řadě
# se vypouští.

import random
#import numpy

#my_array_length = int(input("enter array length: "))
my_array_length = 10
my_list = random.sample (range (1, 100), my_array_length)
result_list = []

for n in range(0,my_array_length):
    if n==(my_array_length-1):
        break

#    x=(my_list[n]+my_list[n+1])/2
#    print(x)

    result_list.append(round((float((my_list[n]+my_list[n+1])/2)),2))

print('\nInput list:\n')
print(my_list)
print('\nResult list:\n')
print(result_list)

#print('\nInput list:\n',*my_list)
#print('\nResult list:\n',*result_list)

```

