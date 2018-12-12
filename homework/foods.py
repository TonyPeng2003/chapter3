foods= ["pizza", "chocolate", "milktea", "meat", "noodles"]
print( "The first three items in the list are "+str(foods[0:3]))
print( "The middle three items in the list are "+str(foods[1:4]))
print( "The last three items in the list are "+str(foods[2:]))



pizzas = ['good pizza','flower pizza','banana pizza']
friends_pizzas = ['good pizza','flower pizza','banana pizza']


for pizza in pizzas:
	print('I like ' + pizza)
print('I like pizzas very much')


pizzas.append('fruit pizza')
friends_pizzas.append('pieapple pizza')


for pizza in pizzas:
    print('My favorite pizzas are: ' + pizza)


for friends_pizza in friends_pizzas:
    print('My friend’s favorite pizzas are: ' + friends_pizza)


for pizza in pizzas:
    print(pizza)



foods = ('chicken','chocalate','pizza','meat','milktea')
for food in foods:
    print(food)
foods[2] = 'cabage'
foods = ('chicken','chocolate','pizza','meat','nuts')
for food in foods:
    print(food)
