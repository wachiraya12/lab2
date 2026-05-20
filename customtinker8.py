import customtkinter as ctk 
import random
class Lab8(ctk.CTk):
    def __init__(self):
        super().__init__()
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        w, h = int(screen_w * 0.70), int(screen_h * 0.60)
        x, y = (screen_w // 2) - (w // 2), (screen_h // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.title("Lab 8: Industrial Telemetry Dashboard")
        ctk.set_appearance_mode("dark")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.info_frame = ctk.CTkFrame(self, fg_color="#1e1e1e")
        self.info_frame. grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=10)
        self.theory_lbl = ctk.CTkLabel(self.info_frame, text="THEORY: Grid weights allow the UI to expand dynamically.", text_color="cyan")
        self.theory_lbl.pack(pady=2)
        self.hint_lbl = ctk.CTkLabel(self. info_frame, text="HINT: Bind critical states to high-contrast colors (like red) for safety.", text_color="gray")
        self.hint_lbl.pack(pady=2)
        self.temp_frame = ctk.CTkFrame(self)
        self.temp_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        ctk.CTkLabel(self.temp_frame, text="Reactor Temp (C)", font=("Roboto", 18, "bold")).pack(pady=10)
        self.temp_bar = ctk.CTkProgressBar(self.temp_frame, height=25)
        self.temp_bar.set(0.2)
        self.temp_bar.pack(padx=20, pady=10, fill="x")
        self.temp_val_lbl = ctk.CTkLabel(self.temp_frame, text="200 ℃", font=("Roboto", 24))
        self.temp_val_lbl.pack(pady=10)
        self.press_frame = ctk.CTkFrame(self)
        self.press_frame.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")
        ctk.CTkLabel(self.press_frame, text="Hydraulic Pressure (PSI)", font=("Roboto", 18, "bold")).pack(pady=10)
        self.press_bar = ctk.CTkProgressBar(self.press_frame, height=25)
        self.press_bar.set(0.5)
        self.press_bar.pack(padx=20, pady=10, fill="x")
        self.press_val_1bl = ctk.CTkLabel(self.press_frame, text="500 PSI", font=("Roboto", 24))
        self.press_val_1bl.pack(pady=10)
        self.monitor_btn = ctk.CTkButton(self, text="START MONITORING", command=self.toggle_monitoring, height=40)
        self.monitor_btn.grid(row=2, column=0, columnspan=2, pady=20)
        self.is_monitoring = False
    def toggle_monitoring(self):
        self.is_monitoring = not self.is_monitoring
        if self.is_monitoring:
            self.monitor_btn.configure(text="STOP MONITORING", fg_color="red", hover_color="#aa0000")
            self.update_sensors()
        else:
            self.monitor_btn.configure(text="START MONITORING", fg_color=["#3B8ED0", "#1F6AA5"])
    def update_sensors (self):
        if not self.is_monitoring: return
        temp_val = random.uniform(0.1, 1.0)
        press_val = random.uniform(0.3, 0.9)
        self.temp_bar.set(temp_val)
        self.press_bar.set(press_val)
        actual_temp = int(temp_val * 1000)
        actual_press = int(press_val * 1000)
        self.temp_val_lbl.configure(text=f"{actual_temp} °C")
        self.press_val_lbl.configure(text=f"{actual_press} PST")
        if temp_val > 0.85:
            self.temp_bar.configure(progress_color="red")
            self.temp_val_lbl.configure(text_color="red")
        else:
            self.temp_bar.configure(progress_color=["#3B8ED0", "#1F6AA5"])
            self.temp_val_lbl.configure(text_color=["black", "white"])
        self.after(500, self.update_sensors)
if __name__ == "__main__":
    app = Lab8()
    app.mainloop()
            
        