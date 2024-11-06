import tkinter as tk
import random
import time

# Function to create a random list
def generate_data():
    global data
    data = [random.randint(1, 100) for _ in range(50)]
    draw_data(data, ['gray' for _ in range(len(data))])

# Function to start bubble sort visualization
def bubble_sort():
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['red' if x == j or x == j + 1 else 'gray' for x in range(len(data))])
                time.sleep(0.05)
                window.update_idletasks()
    draw_data(data, ['green' for _ in range(len(data))])

# Function to draw bars on canvas
def draw_data(data, color_array):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalized_data = [i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
    window.update_idletasks()

# Setting up the main window
window = tk.Tk()
window.title("Bubble Sort Visualization")
window.maxsize(700, 500)
window.config(bg="white")

# Frame for UI controls
frame = tk.Frame(window, bg="white")
frame.place(relx=0.5, rely=0.05, anchor='n')

# Canvas to display sorting
canvas = tk.Canvas(window, width=600, height=380, bg="black")
canvas.pack(pady=20)

# Generate and Start Buttons
tk.Button(frame, text="Generate Data", command=generate_data, bg="lightblue").grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Start Sorting", command=bubble_sort, bg="lightgreen").grid(row=0, column=1, padx=5, pady=5)

# Initial data
data = []
generate_data()

# Run the window loop
window.mainloop()