import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Ініціалізація лічильника для сум від 2 до 12
    sum_counts = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        # Підрахунок кількості кидків для можливих значень сум
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sum_counts[dice_sum] += 1
    # Обчислення ймовірностей для кожної суми
    probabilities = {s: count / num_rolls for s, count in sum_counts.items()}
    return probabilities


def plot_probabilities(probabilities, accuracy):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках N=' + str(accuracy))
    
    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        # Симуляція кидків і обчислення ймовірностей
        probabilities = simulate_dice_rolls(accuracy)

        # Відображення ймовірностей на графіку
        plot_probabilities(probabilities, accuracy)