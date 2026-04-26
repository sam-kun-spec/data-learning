# # dictionary  = an order of {key: value} pairs,
#                 changable , indexed , no duplicate  

capitals = {
    "india": "new delhi",
    "japan": "tokyo"
}

print(capitals)

print(capitals["india"]) # access value by key
print(capitals.get("japan"))

user = input("enter a country: ")



if capitals[user]:
   print("capital found")
else:
   print("capital not found")

# capitals.update({"usa":"washington dc"}) # add key value pair and update value of existing key 
# capitals["germany"] = "berlin" # another way to add key value pair
# capitals.pop("japan") # remove the key value pair
# capitals.popitem() # removes last inserted key value pair
# capitals.clear() # removes all key value pairs 

# keys = capitals.keys() # get all the keys
# print(keys)

# for key in capitals.keys():
#     print(key)

# value  = capitals.values() #get all the values

items = capitals.items() # get all the key value pairs
for key, value in items:
    print(key,":",value)