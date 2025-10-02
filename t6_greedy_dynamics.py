# Adjusting the code to use a dictionary for items instead of a list of tuples.

# Define the items with their cost and calorie value.
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Greedy approach
def greedy_algorithm(items, budget):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    # Sort items by calorie-to-cost ratio in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    for item, details in sorted_items:
        # Реалізувати логіку обирання кращого блюда 
        if details['cost'] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details['calories']
            remaining_budget -= details['cost']

    return total_calories, budget - remaining_budget, chosen_items


# Dynamic Programming approach
def dynamic_programming(items, budget):
    item_names = list(items.keys())

    # Create a DP table where rows represent up to the i-th item and columns represent budget
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]

    # Реалізація побудови таблиці оптимального блюда по калоріям для всіх бюджетів
    for i in range(1, len(items) + 1):
        item = item_names[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp_table[i][w] = max(dp_table[i - 1][w], dp_table[i - 1][w - cost] + calories)
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    # Реалізація отримання оптимального набору страв через використання обчисленої таблиці
    chosen_items = []
    temp_budget = budget
    for i in range(len(items), 0, -1):
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            item = item_names[i - 1]
            chosen_items.append(item)
            temp_budget -= items[item]['cost']

    return dp_table[len(items)][budget], budget - temp_budget, chosen_items


if __name__ == '__main__':
    # Execute both algorithms
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print(greedy_result, dp_result)
