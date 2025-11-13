import json;                            # Import the JSON module to work with JSON data

with open('data.json', 'r') as file:    # Open the JSON file
    data = json.load(file);             # Load its content into a Python dictionary
name = data.get('name');                # Retrieve the value associated with the key 'name'

print(name);                            # Print the retrieved name

print("\nListing additional information:");     # Print a header for additional information
for key, value in data.items():                 # Iterate through all key-value pairs in the dictionary
    if key != 'name':                           # Skip the 'name' key
        print(f"{key}: {value}");               # Print each key and its corresponding value

print("\nListing specific details:");           # Print a header for specific details
specific_keys = ['author', 'license', 'dependencies'];  # Define a list of specific keys to look for
for key in specific_keys:                       # Iterate through the list of specific keys
    if key in data:                             # Check if the key exists in the dictionary
        print(f"{key}: {data[key]}");           # Print the key and its corresponding value

print("\nPrinting only values of the keys:");    # Print a header for values only
for key in specific_keys:                        # Iterate through the list of specific keys
    if key in data:                              # Check if the key exists in the dictionary
        print(data[key]);                        # Print only the value associated with the key