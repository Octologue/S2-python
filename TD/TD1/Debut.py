import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

 # Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
y0 = 100
y1 = CANVAS_HEIGHT - 100
x = CANVAS_WIDTH/2
canvas.create_line(x, y0, x, y1)
canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
#create oval fonctionne comme créer un rectangle avec un cercle à l'intérieur. 

# Fin de votre code

canvas.grid() #ou canvas.pack
root.mainloop()
