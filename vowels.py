#Vowels Finder
#Taking values
states=[]
states_new=[]
states=input("Enter the names of states").split(" ")
for state in range(states):
    for char in range(state):
        if char.lower() not in ("a","e","i","o","u"):
            states_new.append(char)
print(states_new)
