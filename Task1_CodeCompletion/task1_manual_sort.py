# Manual implementation for sorting a list of dictionaries by a specific key

def sort_dicts_by_key(data, key):
    """Sort a list of dictionaries by a given key."""
    return sorted(data, key=lambda x: x[key])

# Example data
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 30}
]

# Sort by age
sorted_people = sort_dicts_by_key(people, "age")

print("Sorted manually by age:")
print(sorted_people)
