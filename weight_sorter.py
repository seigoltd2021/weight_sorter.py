animals = [
    {"name": "собака", "weight": 20},
    {"name": "кошка", "weight": 5},
    {"name": "слон", "weight": 2000},
    {"name": "крыса", "weight": 0.5},
    {"name": "крокодил", "weight": 100},
]

sorted_animals = sorted(animals, key=lambda x: x["weight"])

print("Животные, отсортированные по весу:")
for animal in sorted_animals:
    print(animal["name"], "-", animal["weight"], "кг")
