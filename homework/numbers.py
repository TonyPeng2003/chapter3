for number in range(1,20):
    print(number)


for number in range(1,10000):
    print(number)


numbers= []
for number in range(1,10000):
    numbers.append(number)
print(str(min(numbers))+" and " +str(max(numbers)))
print(str(sum(numbers)))


for number in range(1,20,2):
    print(number)


numbers= []
for number in range(3,30):
    numbers.append(number*3)
print(numbers)


numbers= []
for number in range(1,10):
    numbers.append(number**3)
print(numbers)


numbers= [number**3 for number in range(1,10)]
print(numbers)