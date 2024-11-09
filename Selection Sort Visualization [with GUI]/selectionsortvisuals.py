import tkinter as tk
import random
import time

# Global variables for colors
BACKGROUND_COLOR = "#333333"
BAR_COLOR = "#e05a5a"
SORTED_BAR_COLOR = "#58D68D"
ACTIVE_BAR_COLOR = "#F7DC6F"
WIDTH = 800
HEIGHT = 400

# Initialize the GUI window
window = tk.Tk()
window.title("Selection Sort Visualization")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.config(bg=BACKGROUND_COLOR)

# Create a canvas to draw the bars
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

# Generate random array
array = [random.randint(10, 100) for _ in range(20)]
bar_width = WIDTH // len(array)

def draw_array(array, color_array):
    canvas.delete("all")
    for i, value in enumerate(array):
        x0 = i * bar_width
        y0 = HEIGHT - value * 3
        x1 = (i + 1) * bar_width
        y1 = HEIGHT
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i], outline="")
    window.update_idletasks()

def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        # Highlight the current minimum
        color_array = [SORTED_BAR_COLOR if x < i else BAR_COLOR for x in range(n)]
        color_array[min_index] = ACTIVE_BAR_COLOR
        draw_array(array, color_array)
        time.sleep(0.5)

        for j in range(i + 1, n):
            # Highlight the current comparison
            color_array[j] = ACTIVE_BAR_COLOR
            draw_array(array, color_array)
            time.sleep(0.1)
            if array[j] < array[min_index]:
                min_index = j
            color_array[j] = BAR_COLOR  # Reset color after comparison

        # Swap the minimum element with the first unsorted element
        array[i], array[min_index] = array[min_index], array[i]
        draw_array(array, color_array)
        time.sleep(0.5)

    # Mark all elements as sorted
    draw_array(array, [SORTED_BAR_COLOR] * n)

# Run the selection sort and visualize it
def start_sorting():
    selection_sort(array)

# Button to start the sorting visualization
start_button = tk.Button(window, text="Start Selection Sort", command=start_sorting, bg=BAR_COLOR, fg="white")
start_button.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()