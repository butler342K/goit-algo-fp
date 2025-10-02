import matplotlib.pyplot as plt
import numpy as np

def draw_branch(ax, x, y, size, angle, depth):
    if depth == 0:
        return
    
    cos_a = np.cos(np.radians(angle))
    sin_a = np.sin(np.radians(angle))
    
    # Початок і кінець центральної лінії
    start_x = x - size/2 * sin_a
    start_y = y - size/2 * cos_a
    end_x = x + size/2 * sin_a
    end_y = y + size/2 * cos_a
    
    ax.plot([start_x, end_x], [start_y, end_y], 'brown', linewidth=2)
    
    # Верхня середина
    top_x = x + size/2 * sin_a
    top_y = y + size/2 * cos_a
    
    # Розмір нової гілки
    new_size = size / np.sqrt(2)
    
    # Ліва гілка
    left_angle = angle + 45
    left_x = top_x + new_size/2 * np.sin(np.radians(left_angle))
    left_y = top_y + new_size/2 * np.cos(np.radians(left_angle))
    draw_branch(ax, left_x, left_y, new_size, left_angle, depth - 1)
    
    # Права гілка
    right_angle = angle - 45
    right_x = top_x + new_size/2 * np.sin(np.radians(right_angle))
    right_y = top_y + new_size/2 * np.cos(np.radians(right_angle))
    draw_branch(ax, right_x, right_y, new_size, right_angle, depth - 1)

def main():
    recursion_level = input("Enter the recursion level (e.g., 5): ")
    try:
        recursion_level = int(recursion_level)
        if recursion_level < 0:
            raise ValueError
        elif recursion_level > 15:
            print("Level too high, setting to maximum level 15.")
            recursion_level = 15
    except ValueError:
        print("Invalid input. Using default level 5.")
        recursion_level = 5

    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_aspect('equal')
    ax.axis('off')

    # Побудова дерева
    draw_branch(ax, 0, 0, 1, 0, recursion_level)

    plt.show()

if __name__ == "__main__":
    main()
