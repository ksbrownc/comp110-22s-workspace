"""Demonstrates of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Intialize to an empty dictionary
schools = dict()

# set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NSCU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "Lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key.
schools.pop("Duke")

# test for the existence of a key
if "Duke" in schools: 
    print("Found the key 'Duke in schools")
else:
    print ("No key 'Duke' in schools")
# is_duke_present: bool = "Duke" in schools
# print(f"Duke is present: {is_duke_present}")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of ditionary literals

# Empty dictionary Literal
schools= {} # same as dict()
print(schools)
# Alternatively, initalize keyvalues pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

#What happens when a key does not exist? terminal says a key error
print(schools["UNCC"])
#Example looping over the keys of a dict 
for key in schools: 
    print(f"Key: {key} -> Value: {schools[key]}")