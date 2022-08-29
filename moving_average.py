# Given a series of numbers and a fixed subset size, the first element of the moving average is obtained by taking
# the average of the initial fixed subset of the number series. Then the subset is modified by "shifting forward";
# that is, excluding the first number of the series and including the next value in the subset.

# https://www.geeksforgeeks.org/how-to-calculate-moving-averages-in-python/

# Klouzavý průměr je: Statistická metoda eliminující výkyvy v časových řadách. Počítá se z údajů časové řady tak,
# že se postupně k danému počtu údajů (např. 12 měsíců) přiřazuje vždy jeden údaj následující a první údaj v řadě
# se vypouští.

import random
#import numpy

my_array_length = int(input("enter array length: "))
my_list = random.sample (range (1, 100), my_array_length)
result_list = []

for m in range(0,my_array_length):
    if m==(my_array_length-1):
        break

#    x=(my_list[m]+my_list[m+1])/2
#    print(x)

    result_list.append(round((float((my_list[m]+my_list[m+1])/2)),2))

#print('\nInput list:\n')
#print(my_list)
#print('\nResult list:\n')
#print(result_list)

print('\nInput list:\n',*my_list)
print('\nResult list:\n',*result_list)








