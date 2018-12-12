girlfriends=['Elizabeth','Livia','Lisa','Liv']
print(len(girlfriends))

print("Will you have a date with me, "+girlfriends[0]+" ?")
print("Will you have a date with me, "+girlfriends[1]+" ?")
print("Will you have a date with me, "+girlfriends[2]+" ?")
print("Will you have a date with me, "+girlfriends[3]+" ?")

print("Elizabeth can't come. ")
print("Sad to hear that, "+girlfriends[0]+" .")
print("Elizabeth can't come, "+girlfriends[1]+" .")
print("Elizabeth can't come, "+girlfriends[2]+" .")
print("Elizabeth can't come, "+girlfriends[3]+" .")

girlfriends[0] = "Jenny"
print("Will you have a date with me, "+girlfriends[0]+" ?")
girlfriends.append("Cindy")
girlfriends.insert(0, "Mary")
girlfriends.insert(2, "Linda")
print(len(girlfriends))

print("Will you have a date with me, "+girlfriends[0]+" ?")
print("Will you have a date with me, "+girlfriends[1]+" ?")
print("Will you have a date with me, "+girlfriends[2]+" ?")
print("Will you have a date with me, "+girlfriends[3]+" ?")
print("Will you have a date with me, "+girlfriends[4]+" ?")
print("Will you have a date with me, "+girlfriends[5]+" ?")
print("Will you have a date with me, "+girlfriends[6]+" ?")
print(len(girlfriends))

popped1=girlfriends.pop(1)
print("Sorry "+ popped1+ ", I can only invite two people, maybe coming next time. ")
popped2=girlfriends.pop(2)
print("Sorry "+ popped2+ ", I can only invite two people, maybe coming next time. ")
popped3=girlfriends.pop(3)
print("Sorry "+ popped3+ ", I can only invite two people, maybe coming next time. ")
popped0=girlfriends.pop(0)
print("Sorry "+ popped0+ ", I can only invite two people, maybe coming next time. ")
popped4=girlfriends.pop()
print("Sorry "+ popped4+ ", I can only invite two people, maybe coming next time. ")
print(len(girlfriends))

print("Luckily, you are still invited, "+ girlfriends[0]+ ". ") 
print("Luckily, you are still invited, "+ girlfriends[1]+ ". ") 
len(girlfriends)

del girlfriends[0]
del girlfriends[0]
print(girlfriends)
print(len(girlfriends))
