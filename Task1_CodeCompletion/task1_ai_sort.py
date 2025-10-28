# AI-generated version (GitHub Copilot/Tabnine suggestion)

def sort_dicts_by_key(data, key):
    try:
        data.sort(key=lambda item: item.get(key, 0))
        return data
    except Exception as e:
        print(f"Error: {e}")
        return data

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 19},
    {"name": "Charlie", "age": 30}
]

print("AI-generated sorted list:")
print(sort_dicts_by_key(people, "age"))
