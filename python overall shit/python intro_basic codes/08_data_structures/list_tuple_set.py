#list [] = mutable
#tuple () = immutable , faster than list
#set {} = unordered, no duplicate items , mutable

protien = ["paneer" , "soyachunks", "peanut butter", "high protien oats"]

print(protien)
print(protien[0])
print(protien[-1])

for item in protien:
    print(item,end=" ")

protien[3] = "roasted chickpeas"
protien.append("pumpkin seeds") #adds item at the end
protien.remove("peanut butter") #removes specific item
protien.pop() #removes last item
protien.pop(1) #removes item at index 1
protien.clear() #removes all items

print(protien)




fruits = ("apple", "banana", "mango", "grapes") #  tuple (cannot be changed)


pulses = {"lentils", "chickpeas", "black beans", "kidney beans"} # set (no duplicate items) 

for item in pulses:
    print(item, end=" ") # order not guaranteed , it gonna vary each time

# pulses.add("moong dal") # adds item
# pulses.remove("black beans") # removes specific item
# pulses.clear() # removes all items

# we cannot access items in set by index like list or tuple because it's unordered

if "chickpeas" in pulses:
    print("\nchickpeas are found ")
else:
    print("\nchickpeas are not found ")

user = input("enter a pulses: ")

if user in pulses:
    print(user + " is found in the set.")   