from timeit import repeat
from statistics import mean

def func1():
    arr = [1, 2, 3, 4, 5]
    arr.append(6)

def func2():
    arr = [1, 2, 3, 4, 5]
    arr += [6]




timings = repeat(func2, number=100)

mn = min(timings)
avg = mean(timings)
mx = max(timings)

print("Minimum execution time:", mn)
print("Average execution time:", avg)
print("Maximum execution time:", mx)
