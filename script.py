# Build a cute little game while utilizing variables,
# functions, conditionals, loops and object oriented programming
# /Users/Taelur/Desktop/py-games/script.py

#user_name = input("What is your name? ")
#goals = input("What are your goals? ")
#age = input("How old are you? ")

#print(f"Your name is {user_name}. Your goals are: {goals}. You are {age} years old.")

# Collections - tuples, arrays/lists, dict
# Tuples- immutable
# Lists- mutable
# Dictionaries- key value pairs

# access both values in one variable
size = (100, 200)
# Access elements in a tuple- cant remove or add elements 
#width = size[0]
#height = size[1]
# reassign a tuple-
#new_size = size + (300,)

# to delete a tuple - del new_sieze
#print(new_size)

#does_contain = 100 in size # print if value is found in tuple 
#print(does_contain) # check if tuple, array or list contain an element
#print(len(new_size))#- prints the length of elements in a tuple
#print(max(new_size))# prints the largest element in a tuple
#print(min(new_size))# prints the minimum element in a tuple

# list of built in movement
movement = [5, -1, 2, 3, -1]
movement[0] = 1
#print(movement[0])
#rint(movement)

# Access element in list
#movement[-1] = 4343243

# Add element
#movement.append(3)

# Add list to list

#movement + [3]

#updated = movement + ["Hello", "Hi"]
#print(type(movement[0]))
#print(updated)

# remove element
#movement.remove(2)

#print(movement)

my_dict = {"Player1": "Andy", "Player2": "Susan", "Player3": "Karen"}

get_key = my_dict.get("Player1") # return value of specified key
print(get_key)

#get_popped = my_dict.pop("Player2")

#retrieve all values from a dict
all_val = my_dict.values()
print(all_val)
print("Here is how to update a dict:")
my_dict.update({"Player5": "Daniel"})

tupled_items = my_dict.items()

print(f"Here are tupled pairs from dict:\n{tupled_items}\n")

all_keys = my_dict.keys()

print(f"Here all the keys of the dict: {all_keys}")

# Retrieve value of key
player1 = my_dict["Player1"]
print(player1)




