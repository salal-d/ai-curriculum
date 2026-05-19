def greet(name):
    print(f"Hello, {name}! Welcome to the AI curriculum.")

greet ("Tyler")
greet ("Ada")
greet ("Claude")


def calculate_project_Cost(days,daily_rate):
    total = days * daily_rate
    return total

project_a = calculate_project_Cost(5, 1500)
project_b = calculate_project_Cost(12, 2000)

print(f"Project A Cost: ${project_a}")
print(f"Project B Costs: ${project_b}")

