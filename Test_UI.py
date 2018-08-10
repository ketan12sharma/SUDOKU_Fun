import tkinter as tk

window=tk.Tk()

window.title("SUDOKU")
window.geometry("450x450")
canvas= tk.Canvas(window)
canvas.pack()
canvas.create_line(0,50,0,50)
window.mainloop()   