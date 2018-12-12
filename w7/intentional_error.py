name=['Tommy','Livia','Lisa','Peter']
print(len(name))

print("You are my best friend, would you like to have dinner with me, "+name[0]+" ?")
print("You are my best friend, would you like to have dinner with me, "+name[1]+" ?")
print("You are my best friend, would you like to have dinner with me, "+name[2]+" ?")
print("You are my best friend, would you like to have dinner with me, "+name[3]+" ?")

print("Tommy can't come. ")
print("Sad to hear that, "+name[0]+" .")
print("Tommy can't come, "+name[1]+" .")
print("Tommy can't come, "+name[2]+" .")
print("Tommy can't come, "+name[3]+" .")

name[0] = "Jenny"
print("You are my best friend, would you like to have dinner with me, "+name[0]+" ?")
name.append("Tom")
name.insert(0, "Jerry")
name.insert(2, "Billy")
print(len(name))

print("You are my best friend, would you like to have dinner with me, "+name[0]+" ?")
print("You are my best friend, would you like to have dinner with me, "+name[1]+" ?")
print("You are my best friend, would you like to have dinner with me, "+name[2]+" ?")
print("You are my best friend, would you like to have dinner with me, "+name[3]+" ?")
print("You are my best friend, would you like to have dinner with me, "+name[4]+" ?")
print("You are my best friend, would you like to have dinner with me, "+name[5]+" ?")
print("You are my best friend, would you like to have dinner with me, "+name[6]+" ?")
print(len(name))

popped1=name.pop(1)
print("Sorry "+ popped1+ ", I can only invite two people, maybe coming next time. ")
popped2=name.pop(2)
print("Sorry "+ popped2+ ", I can only invite two people, maybe coming next time. ")
popped3=name.pop(3)
print("Sorry "+ popped3+ ", I can only invite two people, maybe coming next time. ")
popped0=name.pop(0)
print("Sorry "+ popped0+ ", I can only invite two people, maybe coming next time. ")
popped4=name.pop()
print("Sorry "+ popped4+ ", I can only invite two people, maybe coming next time. ")
print(len(name))

print("Luckily, you are still invited, "+ name[0]+ ". ") 
print("Luckily, you are still invited, "+ name[1]+ ". ") 
len(name)

del name[0]
del name[0]
print(name)
print(len(name))

print(name[7])