first_name = "Ada"
last_name = "Lovelace"

full_name = f"{first_name} {last_name}"
print(full_name)
print(full_name.upper())
print(full_name.lower())
print(len(full_name))

price = 49.99
quantity = 3
total = price * quantity 
print(total)



client = { 
    "name": "salal design",
    "industry": "design",
    "employees": 1,
    "location": "vancouver",
    "tools_needed": [
        "chatbot", "list", 
        "summerizer", "classifier", "indexer"]
}

print(client["tools_needed"][-2])
print(client)