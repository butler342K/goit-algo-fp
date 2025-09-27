import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def pithagoras_tree(ax, bottom_left, size, angle, level):
    if level == 0:
        return
    
    # Рахуємо координати чотирьох кутів квадрата
    cos_a = np.cos(np.radians(angle))
    sin_a = np.sin(np.radians(angle))
    
    bottom_right = [bottom_left[0] + size * cos_a, bottom_left[1] + size * sin_a]
    top_right = [bottom_right[0] - size * sin_a, bottom_right[1] + size * cos_a]
    top_left = [bottom_left[0] - size * sin_a, bottom_left[1] + size * cos_a]
    
    # Малюємо квадрат
    square = patches.Polygon([bottom_left, bottom_right, top_right, top_left], 
                           fill=True, edgecolor='green', facecolor='lightgreen')
    ax.add_patch(square)
    
    # Рахуємо координати вершини трикутника
    mid_top = [(top_left[0] + top_right[0]) / 2, (top_left[1] + top_right[1]) / 2]
    triangle_height = size / 2
    
    # Вершина трикутника
    apex_x = mid_top[0] - triangle_height * sin_a
    apex_y = mid_top[1] + triangle_height * cos_a
    triangle_apex = [apex_x, apex_y]
    
    # Новий розмір для наступного рівня
    new_size = size / np.sqrt(2)
    
    # Рекурсивно малюємо два нових дерева
    pithagoras_tree(ax, top_left, new_size, angle + 45, level - 1)
    pithagoras_tree(ax, triangle_apex, new_size, angle - 45, level - 1)

def naked_pithagoras_tree(ax, bottom_left, size, angle, level):
    if level == 0:
        return
    
    # Рахуємо координати чотирьох кутів квадрата
    cos_a = np.cos(np.radians(angle))
    sin_a = np.sin(np.radians(angle))
    
    bottom_right = [bottom_left[0] + size * cos_a, bottom_left[1] + size * sin_a]
    top_right = [bottom_right[0] - size * sin_a, bottom_right[1] + size * cos_a]
    top_left = [bottom_left[0] - size * sin_a, bottom_left[1] + size * cos_a]
    mid_top = [(top_left[0] + top_right[0]) / 2, (top_left[1] + top_right[1]) / 2]
    mid_bottom = [(bottom_left[0] + bottom_right[0]) / 2, (bottom_left[1] + bottom_right[1]) / 2]
    # Малюємо центральну лінію квадрата
    p = patches.Polygon([mid_bottom, mid_top], 
                           fill=False, edgecolor='brown', linewidth=1)
    ax.add_patch(p)
    
    # Рахуємо координати вершини трикутника
    mid_top = [(top_left[0] + top_right[0]) / 2, (top_left[1] + top_right[1]) / 2]
    triangle_height = size / 2
    
    # Вершина трикутника
    apex_x = mid_top[0] - triangle_height * sin_a
    apex_y = mid_top[1] + triangle_height * cos_a
    triangle_apex = [apex_x, apex_y]
    
    # Новий розмір для наступного рівня
    new_size = size / np.sqrt(2)
    
    # Рекурсивно малюємо два нових дерева
    naked_pithagoras_tree(ax, top_left, new_size, angle + 45, level - 1)
    naked_pithagoras_tree(ax, triangle_apex, new_size, angle - 45, level - 1)

def main():
    recursion_level = input("Enter the recursion level (e.g., 5): ")
    naked = input("Do you want a naked tree? (Y/N): ").strip().lower()
    if naked == 'y':
        naked = True
    else:
        naked = False
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
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_aspect('equal')
    ax.set_axis_off()
    if naked:
        naked_pithagoras_tree(ax, [0, 0], 1, 0, recursion_level)
    else:
        pithagoras_tree(ax, [0, 0], 1, 0, recursion_level)
    ax.set_xlim(-4, 5)
    ax.set_ylim(-3, 6)
    plt.show()

if __name__ == "__main__":
    main()