import tkinter as tk

ventana = tk.Tk()
ventana.geometry(”300x400“)
pantalla = tk.Entry(ventana, font=(“Arial”, 20))
pantalla.pack(pady=10)
boton1 = tk.Button(ventana, text=”1”,font=(”Arial”, 14))
boton1 .pack(pady=5)
ventana.mainloop()