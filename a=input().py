import random

rundom_nambers = [random.randint(1,10000) for i in range(10)]
print(rundom_nambers)
print(sorted(rundom_nambers))
print(min(rundom_nambers))
print(max(rundom_nambers))

sum = 0

for i in rundom_nambers:
    sum += i

print(sum)
