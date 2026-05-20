import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
import time
class EnergyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart City Grid Optimizer v1.0")
        self.root.geometry("800x600")
        self.header = tk.Label(root, text="ENERGY DEMAND PREDICTOR", font=('Arial', 18, 'bold'), fg='#00d1b2')
        self.header.pack(pady=10)
        self.input_frame = ttk. LabelFrame(root, text=" Grid Configuration ")
        self.input_frame.pack(padx=20, pady=10, fill="x")
        tk.Label(self.input_frame, text="Select City Zone:").grid(row=0, column=0, padx=5, pady=5)
        self.zone_var = ttk.Combobox(self.input_frame, values=["Industrial", "Residential"])
        self.zone_var.current(0)
        self.zone_var.grid(row=0, column=1, padx=5, pady=5)
        tk. Label(self.input_frame, text="Current Temp (C):").grid(row=0, column=2, padx=5, pady=5)
        self.temp_slider = ttk.Scale(self.input_frame, from_= 10, to=45, orient="horizontal")
        self.temp_slider.grid(row=0, column=3, padx=5, pady=5)
        self.run_btn = tk.Button(root, text="OPTIMIZE GRID", command=self.process_logic, bg='#00d1b2', fg='white', font=('bold'))
        self.run_btn.pack (pady=10)
        self.progress = ttk.Progressbar(root, length=400, mode='determinate')
        self.progress.pack(pady=5)
        self.fig, self.ax = plt.subplots(figsize=(5, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()
    def process_logic(self):
         for i in range(1, 101, 10):
             self.progress['value'] = i
             self.root.update_idletasks()
             time.sleep(0.05)
         X = np.array([[20], [25], [30], [35], [40]])
         y = np.array([400, 450, 520, 600, 710]) if self.zone_var.get() == "Industrial" else np.array([100, 200, 350, 600, 850])
         model = LinearRegression().fit(x, y)
         current_temp = self.temp_slider.get()
         pred = model.predict([ [ current_temp] ])
         self.ax.clear()
         self.ax.scatter(x, y, color='blue', label='Historical Data')
         self.ax.plot(X, model.predict(X), color='red', label='AI Trendline')
         self.ax.scatter([current_temp], [pred], color='green', s=100, label='Prediction')
         self.ax.set_title(f"Predicted Load: {pred[0]:.2f} MW")
         self.ax.legend()
         self.canvas.draw()
root = tk.Tk()
app = EnergyApp(root)
root.mainloop()
            